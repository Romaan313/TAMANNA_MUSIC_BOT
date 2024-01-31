from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5874825438"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/e642e121a9d93e1ac13ca.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/ebb0d85faab06c034ed4c.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+OwXlutqNgoUyYzJl")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/l_DW_l")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5874825438").split()))


FAILED = "https://graph.org/file/a46ef14291618f5d5e93e.jpg"
