import os
import sys
import time
from datetime import datetime
from config.bot_config import BotConfig
import logging.config
import csv
from slack_sdk import WebClient, errors


# logging setting
logging_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "logging.conf")
os.makedirs(BotConfig.LOG_PATH, exist_ok=True)
logging.config.fileConfig(fname=logging_config_path,
                          disable_existing_loggers=True,
                          defaults={
                              'app_name': BotConfig.BOT_NAME,
                              'log_path': f"{os.path.join(BotConfig.LOG_PATH,BotConfig.BOT_NAME)}"
                          }
                          )

client = WebClient(token=BotConfig.BOT_USER_OAUTH_TOKEN)


def delete_messages(channel_id, channel_name, start_timestamp, end_timestamp):
    error_occurred_num = 0
    while True:
        try:
            # 특정 시점 이전의 메시지 가져오기
            result = client.conversations_history(channel=channel_id, oldest=start_timestamp, latest=end_timestamp)
            if not result["ok"]:
                break
            messages = result["messages"]
            for message in messages:
                # client.chat_delete(channel=channel_id, ts=message["ts"])    # 메시지 삭제 요청
                logging.info(f"{channel_name} - Deleted message: {message['ts']} | {message['text']}")
                time.sleep(1)
        except errors.SlackApiError as e:
            if error_occurred_num < 10:
                error_occurred_num += 1
                logging.error(f"Error occurred: {error_occurred_num} | {e}")
                logging.info("sleep 10 seconds...")
                time.sleep(10)
                continue
            else:
                break


def get_channels_info():
    f = open(BotConfig.CHANNELS_INFO_FILEPATH, 'r', newline='', encoding="UTF8")
    reader = csv.reader(f, delimiter=',')
    channels_dictionary = {}
    for line in reader:
        if not line:
            break
        if len(line) != 2:
            logging.error("wrong format: channels_info.csv. Please write like this: [CHANNEL ID],[CHANNEL NAME]")
            sys.exit(1)
        channels_dictionary[line[0]] = line[1]

    logging.info("COMPLETE TO READ channels_info.csv")
    logging.info(channels_dictionary)
    return channels_dictionary


if __name__ == "__main__":
    now = datetime.now()
    # 현재 시점 기준 월 1일 설정
    now_month_firstday = int(datetime(now.year, now.month, 1).timestamp())
    # oldest_timestamp = now_month_firstday
    oldest_timestamp = int(datetime(2020, 1, 1).timestamp())
    channels = get_channels_info()
    for id, name in channels.items():
        logging.info(f"{name}")
        delete_messages(id, name, oldest_timestamp, now_month_firstday)   # 메시지 삭제 함수 호출
