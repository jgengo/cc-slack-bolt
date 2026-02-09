import re

from slack_bolt import App

from {{cookiecutter.__pn}}.listeners.messages.hi_titus import hi_titus


def register(app: App) -> None:
    app.message(
        re.compile(r"^(hi|hello|hey) titus$", re.IGNORECASE)
    )(hi_titus)  # sample message handler