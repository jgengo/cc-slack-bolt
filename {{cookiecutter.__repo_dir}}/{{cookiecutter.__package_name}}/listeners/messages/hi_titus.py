from logging import Logger
from typing import Any

from slack_bolt import BoltContext, Say
from slack_sdk import WebClient

from {{cookiecutter.__pn}}.common.helpers import reply_emoji


def hi_titus(context: BoltContext, say: Say, client: WebClient, message: dict[str, Any], logger: Logger) -> None:
    try:
        greeting = context['matches'][0]
        say(f"{greeting}, how are you?")
        reply_emoji(client, message, "wave")
    except Exception as e:
        logger.error(e)