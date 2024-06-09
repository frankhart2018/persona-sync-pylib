import os


QUEUE_NAME = os.getenv("GEMINI_MESSAGING_QUEUE_NAME", "gemini-messaging")
RABBIT_HOST = os.getenv("RABBIT_HOST", "localhost")
RABBIT_PORT = os.getenv("RABBIT_PORT", 5672)

LOGGER_URL = os.getenv("LOGGER_URL", None)
LOGGER_TOKEN = os.getenv("LOGGER_TOKEN", None)

MONGO_HOST = os.getenv("MONGO_HOST", "mongodb://localhost:27017/")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "chat-agents")
PROMPT_INPUTS_COLLECTION = os.getenv("PROMPT_INPUTS_COLLECTION", "prompt-inputs")

MAX_INTERACTIONS = 4

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
