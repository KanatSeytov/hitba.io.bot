import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

admins = [
    332783067
]

USER = str(os.getenv('MONGO_USER'))
PASSWORD = str(os.getenv('MONGO_PASSWORD'))
IP = str(os.getenv('MONGO_IP'))

MONGO_CONNECTION_KEY = f'mongodb+srv://{USER}:{PASSWORD}@{IP}/?retryWrites=true&w=majority'