import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHRIS_ID = os.getenv("CHRIS_ID")
SERVER = os.getenv("BOT_SERVER")