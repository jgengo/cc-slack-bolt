import logging
import os 

from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

from {{cookiecutter.__pn}}.listeners import register_listeners

load_dotenv()
logging.basicConfig(level=logging.DEBUG)


app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    client=WebClient(
        base_url=os.getenv("SLACK_API_URL", "https://slack.com/api"),
        token=os.getenv("SLACK_BOT_TOKEN"),
    ),
)


register_listeners(app)

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
    handler.start()