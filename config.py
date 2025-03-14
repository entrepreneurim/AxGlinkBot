
import os
from os import environ
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7886196938:AAHCfvYaJ_ryOlm0WZbjIMtKeB-ldJqaIvM")  

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27705761"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "822cb334ca4527a134aae97f9fe44fd6")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002399781553"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6987158459"))

#Port
PORT = os.environ.get("PORT", "3732")

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "AxomBotz")
JOIN_REQS_DB = os.environ.get("JOIN_REQS_DB", DB_URI)
JOIN_REQS_DB2 = os.environ.get("JOIN_REQS_DB2", DB_URI)

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001993981315"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002347474968"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))


#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "30"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>𝖨 𝖺𝗆 𝗃𝗎𝗌𝗍 𝗅𝗂𝗇𝗄 𝗌𝗁𝖺𝗋𝗂𝗇𝗀 𝖻𝗈𝗍 𝖻𝗒 𝖠𝗇𝗂𝗆𝖾𝗑𝖦𝖺𝗅𝗅𝖾𝗋𝗒⚡.</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6987158459").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE", "<b><blockquote>›› 𝖧𝖾𝗒 {mention} ×</blockquote>     𝖧𝖾𝗋𝖾 𝗂𝗌 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄! 𝖢𝗅𝗂𝖼𝗄 𝖻𝖾𝗅𝗈𝗐 𝗍𝗈 𝗉𝗋𝗈𝖼𝖾𝖾𝖽.</b>"
)

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = ""

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
