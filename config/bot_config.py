
import os
from dotenv import load_dotenv

load_dotenv()


class BotConfig:
    BOT_NAME = os.getenv("BOT_NAME", "SlackMessageCleaner")
    # APP_ENV = os.getenv("BOT_ENV", "dev")   # dev, prod
    LOG_PATH = os.getenv("LOG_PATH", './logs/')
    CHANNELS_INFO_FILEPATH = "./channels_info.csv"
    BOT_USER_OAUTH_TOKEN = os.getenv("BOT_USER_OAUTH_TOKEN", "")


bot_config = BotConfig()
