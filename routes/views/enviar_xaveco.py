from slack_bolt import App

from features.xaveco import Xaveco

VIEW = {
    "type": "modal",
    "callback_id": "enviar_xaveco",
    "title": {
        "type": "plain_text",
        "text": "Demo1",
        "emoji": True
    },
    "submit": {
        "type": "plain_text",
        "text": "Submit",
        "emoji": True
    },
    "close": {
        "type": "plain_text",
        "text": "Cancel",
        "emoji": True
    },
    "blocks": [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Bora xavecar",
                "emoji": True
            }
        },
        {
            "block_id": "person",
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":heart: Para quem vai o seu xaveco? :heart:"
            },
            "accessory": {
                "type": "users_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select a user",
                    "emoji": True
                },
                "action_id": "enviar_xaveco-user-action"
            }
        },
        {
            "block_id": "message",
            "type": "input",
            "element": {
                "type": "plain_text_input",
                "action_id": "enviar_xaveco-message-action",
            },
            "label": {
                "type": "plain_text",
                "text": "Qual a mensagem de amor? :awesome:",
                "emoji": True
            },
        }
    ]
}


def set_routes(app: App):
    @app.action('enviar_xaveco-user-action')
    def enviar_xaveco_user_action(ack):
        ack()

    @app.action('enviar_xaveco-message-action')
    def enviar_xaveco_message_action(ack):
        ack()

    @app.view('enviar_xaveco')
    def enviar_xaveco_submission(ack, body, client, view):
        ack('preparando seu xaveco')
        person = view['state']['values']['person']['enviar_xaveco-user-action']['selected_user']
        message = view['state']['values']['message']['enviar_xaveco-message-action']['value']
        ack()  # close modal

        if person[0] == '@':
            person = person[1:]

        Xaveco(app.client, ack).enviar_xaveco(person, message)
