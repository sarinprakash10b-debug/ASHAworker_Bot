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
