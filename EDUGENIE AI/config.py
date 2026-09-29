import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "EduGenie"
APP_VERSION = "1.0.0"

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

EXPLANATION_BACKEND = os.getenv(
    "EXPLANATION_BACKEND",
    "gemini"
).lower().strip()

LOCAL_MODEL_NAME = os.getenv(
    "LOCAL_MODEL_NAME",
    "MBZUAI/LaMini-Flan-T5-783M"
)

MAX_OUTPUT_TOKENS = int(
    os.getenv("MAX_OUTPUT_TOKENS", "2048")
)

TEMPERATURE = float(
    os.getenv("TEMPERATURE", "0.3")
)