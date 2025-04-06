import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7310893289:AAG2kK1vyEuhyM3UdVdppoipLqNd4VQ1wfE")


    # Get from my.telegram.org (or @Vbhgvbgf_bot)
    APP_ID = int(os.environ.get("APP_ID", "28962746"))
    API_HASH = os.environ.get("API_HASH", "727457f88d661b08e636188a949cd9f3")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7228049098").split())
