import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHRIS_ID = os.getenv("CHRIS_ID")
SERVER = os.getenv("BOT_SERVER")
TEST_ID = os.getenv("TEST_ID")

# Roles
SERVER_ADMIN = "Master of Magics"
BLOOD_BOWL_ADMIN = "League Manager"
