from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

BOT_TOKEN = environ.get("BOT_TOKEN", None)
API_ID = int(environ.get("API_ID", 6))
API_HASH = environ.get("API_HASH", "b44886a2a17af2920844c6ddcf9a21a2")
API_ID1 = int(environ.get("API_ID1", 6))
API_HASH1 = environ.get("API_HASH1", "b44886a2a17af2920844c6ddcf9a21a2")
SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "").split()]
LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
BASE_DB = environ.get("BASE_DB", None)
MONGO_URL = environ.get("MONGO_URL", None)
ARQ_API_URL = environ.get("ARQ_API_URL", None)
ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
COMMAND_PREFIXES = environ.get("COMMAND_PREFIXES", None)



