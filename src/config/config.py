import os
from dotenv import load_dotenv

# laad .env
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

LOGS_DIR = "logs"
JSON_SAVE_FILE_LOCATION = "data/parsed_resume.json"
LLM_MODEL_NAME = "openai/gpt-oss-120b"




