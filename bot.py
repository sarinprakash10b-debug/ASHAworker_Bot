import os
import csv
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from groq import Groq

# -------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# -------------------------------------------------
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN missing in .env")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY missing in .env")

# -------------------------------------------------
# GROQ CLIENT CONFIGURATION
# -------------------------------------------------
client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "llama-3.1-8b-instant"  # Stable + Free + Fast

# -------------------------------------------------
# LANGUAGE-SPECIFIC DISCLAIMERS
# -------------------------------------------------
DISCLAIMER_TEXT = {
    "en": "⚠️ This information is for guidance only. Please consult ANM/PHC/Doctor for confirmation.",
    "hi": "⚠️ यह जानकारी केवल मार्गदर्शन के लिए है। कृपया पुष्टि के लिए एएनएम/पीएचसी/डॉक्टर से परामर्श करें।",
    "ta": "⚠️ இந்த தகவல் வழிகாட்டுதலுக்காக மட்டுமே. உறுதிப்படுத்த ANM/PHC/மருத்துவரை அணுகவும்.",
    "ml": "⚠️ ഈ വിവരങ്ങൾ മാർഗനിർദേശത്തിനായി മാത്രമാണ്. സ്ഥിരീകരണത്തിന് ANM/PHC/ഡോക്ടറെ സമീപിക്കുക."
}

# -------------------------------------------------
# MULTILINGUAL PROMPT BUILDER
# -------------------------------------------------
def build_prompt(question: str, language: str) -> str:
    language_map = {
        "en": "Respond in English.",
        "hi": "Respond in Hindi.",
        "ta": "Respond in Tamil.",
        "ml": "Respond in Malayalam."
    }

    lang_instruction = language_map.get(language, "Respond in English.")

    return (
        "You are a health assistant for ASHA workers in India. "
        "Provide only basic health information. "
        "Do NOT diagnose diseases or prescribe medicines. "
        "Always advise consulting ANM, PHC, or a qualified doctor. "
        f"{lang_instruction}\n\n"
        f"Question: {question}"
    )

# -------------------------------------------------
# GROQ QUERY FUNCTION
# -------------------------------------------------
def ask_groq(prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a safe medical guidance assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print("GROQ ERROR:", e)
        return ""

# -------------------------------------------------
# TELEGRAM COMMAND HANDLERS
# -------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello ASHA Worker 👋\n\n"
        "Commands:\n"
        "/ask – English\n"
        "/ask_hi – हिंदी\n"
        "/ask_ta – தமிழ்\n"
        "/ask_ml – മലയാളം\n"
        "/log – Log patient visit"
    )

async def ask_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text.split()[0]
    language = "en"

    if command == "/ask_hi":
        language = "hi"
    elif command == "/ask_ta":
        language = "ta"
    elif command == "/ask_ml":
        language = "ml"

    question = " ".join(context.args)

    if not question:
        examples = {
            "en": "/ask What are danger signs during pregnancy?",
            "hi": "/ask_hi गर्भावस्था के दौरान खतरे के संकेत क्या हैं?",
            "ta": "/ask_ta கர்ப்பகாலத்தில் அபாய அறிகுறிகள் என்ன?",
            "ml": "/ask_ml ഗർഭകാലത്തിലെ അപകട സൂചനകൾ എന്തൊക്കെയാണ്?"
        }
        await update.message.reply_text(f"Example:\n{examples[language]}")
        return

    prompt = build_prompt(question, language)
    answer = ask_groq(prompt)

    disclaimer = DISCLAIMER_TEXT.get(language, DISCLAIMER_TEXT["en"])

    if answer:
        answer = f"{answer}\n\n{disclaimer}"
    else:
        answer = disclaimer

    await update.message.reply_text(answer)

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = " ".join(context.args)

    if not data:
        await update.message.reply_text(
            "Usage:\n"
            "/log Name, Age, Symptoms, Notes\n\n"
            "Example:\n"
            "/log Sita Devi, 26, swelling of legs, referred to PHC"
        )
        return

    file_exists = os.path.isfile("patient_logs.csv")

    with open("patient_logs.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["telegram_user", "patient_details"])
        writer.writerow([update.effective_user.username, data])

    await update.message.reply_text("✅ Patient visit logged successfully.")

# -------------------------------------------------
# MAIN APPLICATION
# -------------------------------------------------
def main():
    print("Starting ASHA Health Assistant Bot (Groq backend)...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask_handler))
    app.add_handler(CommandHandler("ask_hi", ask_handler))
    app.add_handler(CommandHandler("ask_ta", ask_handler))
    app.add_handler(CommandHandler("ask_ml", ask_handler))
    app.add_handler(CommandHandler("log", log))

    print("Bot is running. Waiting for messages...")
    app.run_polling()

if __name__ == "__main__":
    main()
