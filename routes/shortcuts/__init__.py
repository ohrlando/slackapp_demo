from slack_bolt import App
from slack_sdk import WebClient

from routes.views import enviar_xaveco


def set_routes(app: App):
    @app.shortcut('modal_enviar_xaveco')
    def modal_enviar_xaveco(ack, body, client: WebClient):
        # Acknowledge the command request
        ack()
        # Call views_open with the built-in client
        client.views_open(
            # Pass a valid trigger_id within 3 seconds of receiving it
            trigger_id=body["trigger_id"],
            # View payload
            view=enviar_xaveco.VIEW
        )
