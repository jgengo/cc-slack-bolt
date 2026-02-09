from slack_bolt import App

from {{cookiecutter.__pn}}.listeners import messages

def register_listeners(app: App) -> None:
    messages.register(app)