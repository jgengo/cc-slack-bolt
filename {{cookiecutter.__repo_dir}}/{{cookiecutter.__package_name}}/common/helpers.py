from typing import Any

from slack_sdk import WebClient

def reply_emoji(client: WebClient, message: dict[str, Any], emoji: str) -> None:
    client.reactions_add(channel=message['channel'], timestamp=message['ts'], name=emoji)
