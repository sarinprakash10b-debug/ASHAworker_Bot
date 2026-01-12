# ASHA Health Assistant Telegram Bot

This project is a Telegram-based AI assistant designed to support ASHA workers by providing basic medical guidance and enabling structured patient visit logging.

---

## Features

- AI-powered health guidance using Groq LLM
- Multilingual support (English, Hindi, Tamil, Malayalam)
- Ethical AI safeguards (no diagnosis or prescriptions)
- Patient visit logging using CSV-based storage
- Secure API key management using environment variables

---

## Technology Stack

- Python
- Telegram Bot API
- Groq Large Language Model (llama-3.1-8b-instant)
- CSV file as lightweight database

---

## Commands

| Command | Description |
|-------|------------|
| `/start` | Show available commands |
| `/ask` | Ask health questions in English |
| `/ask_hi` | Ask health questions in Hindi |
| `/ask_ta` | Ask health questions in Tamil |
| `/ask_ml` | Ask health questions in Malayalam |
| `/log` | Log patient visit details |

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/sarinprakash10b-debug/ASHAworker_Bot.git
   cd ASHAworker_Bot

## Ethical AI Statement

This project was developed with a strong emphasis on ethical use of Artificial Intelligence, particularly due to its application in a healthcare-adjacent context involving ASHA workers.

## Medical Safety and Responsibility

The AI assistant is designed strictly as a decision-support and informational tool. It does not diagnose diseases, recommend treatments, or prescribe medication. The system prompt explicitly restricts the AI model to provide only basic health awareness and guidance. Every response includes a medical disclaimer advising users to consult qualified healthcare professionals such as ANMs, PHCs, or doctors for confirmation and treatment. This ensures that clinical decision-making remains under human medical authority.

## Accuracy and Misuse Prevention

To minimize the risk of misinformation, the AI responses are constrained through carefully designed prompts that limit output to general health education. The bot discourages self-medication and reinforces referral to official healthcare channels. The system avoids automated decision-making and does not provide emergency instructions, ensuring responsible use in real-world settings.

## Data Privacy and Protection

The project follows data minimization principles. No sensitive personal identifiers such as Aadhaar numbers, phone numbers, or addresses are collected. Patient visit data is stored locally in a CSV file and is not transmitted to external servers. API credentials are managed securely using environment variables and are never hard-coded or exposed in the public repository.

## Transparency and User Awareness

Users are clearly informed that the information provided is for guidance only. Medical disclaimers are displayed in the user’s selected local language to ensure clarity and comprehension. This transparency helps users understand the limitations of the AI system and prevents over-reliance on automated outputs.

## Ethical Deployment

The system is intended to support, not replace, frontline healthcare workers. It respects human oversight, promotes responsible referrals, and aligns with public health ethics. The design prioritizes accessibility, safety, and accountability, making it suitable for educational and support purposes in community healthcare contexts.
