import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID"," 5940604852"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/2ac1c953d54544cc79dda.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkADTK1DD1FYSGjOCImJjT6MrB7XDjcpimZU2-QGnqrltifkXAwPGm8K0-y3aTLp-UxEa08JifPNhDQQlkUdXFhMNch_N1DNgudOco1uJZZkbBxMU3ZwWN2-QrTncat5lLa77nisH4s0qdqTJwzJgB9VNHP0dZtWmsUutMRfQIk97kmhkL09eW0mvuD9u6Fr0NibIlTiZoBJKbuKXilYnlGGsfJETyFAeCuZaaLJPahNLRaQAzKXR-uoN77d0HjycIvtmYw3L4qeOunZxEWfwyfV_p-9q_NT21uiMqAlgnW9P5FDq8zvfDojXwdHnyv3Ql9H4nGbRViF_7kRpmr_TMwNQAAAAF2DKVvAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
