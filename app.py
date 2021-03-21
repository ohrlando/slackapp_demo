import os
from routes import actions, commands, events, messages, shortcuts, views

from slack_bolt import App


def create_app():
    app = App(
        token=os.environ.get("SLACK_BOT_TOKEN"),
        signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
    )

    actions.set_routes(app)
    commands.set_routes(app)
    events.set_routes(app)
    messages.set_routes(app)
    shortcuts.set_routes(app)
    views.set_routes(app)

    return app
