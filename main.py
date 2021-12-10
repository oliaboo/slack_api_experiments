from slack import WebClient
from slack.errors import SlackApiError

import time

client = WebClient(token='<your token>')

retry_count = 3
time_betw_retry = 2


def retry(func):
    def wrapper():
        for i in range(retry_count):
            try:
                func()
            except Exception as e:
                print(e)
                time.sleep(time_betw_retry)
    return wrapper


@retry
def send_message_hello():
    response = client.chat_postMessage(
        channel='#random',
        text="Hello hello!")
    assert response["message"]["text"] == "Hello hello!"


@retry
def send_message_bye():
    response = client.chat_postMessage(
        channel='#random',
        text="Bye!")
    assert response["message"]["text"] == "Bye!"


if __name__ == "__main__":
    send_message_bye()

# try:
#     response = client.chat_postMessage(
#         channel='#random',
#         text="Hello hello!")
#     assert response["message"]["text"] == "Hello hello!"
# except SlackApiError as e:
#     # You will get a SlackApiError if "ok" is False
#     assert e.response["ok"] is False
#     assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
#     print(f"Got an error: {e.response['error']}")

# Uploading files:
# try:
#     filepath="./tmp.txt"
#     response = client.files_upload(
#         channels='#random',
#         file=filepath)
#     assert response["file"]  # the uploaded file
# except SlackApiError as e:
#     # You will get a SlackApiError if "ok" is False
#     assert e.response["ok"] is False
#     assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
#     print(f"Got an error: {e.response['error']}")
