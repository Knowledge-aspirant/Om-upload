import os

API_ID = API_ID = 22495153

API_HASH = os.environ.get("API_HASH", "34096b38e2f6c4d47ffc593cda42e4cd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6920580702:AAEpdOmEHcEqP5yJKIMH3Zld5l60EfB21Po")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 6153627043))

LOG = -1002095596885

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS","6153627043", "6332786656").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
