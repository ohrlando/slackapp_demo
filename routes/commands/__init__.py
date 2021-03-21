from datetime import datetime

from slack_bolt import App, Say, Ack

from features.time import Time
from features.xaveco import Xaveco


def set_routes(app: App):
    @app.command('/xaveco')
    def send_xaveco(ack: Ack, say: Say, command: dict):
        ack('preparando seu xaveco')
        person, message = command.get('text', '').split(' ', 1)

        if person[0] == '@':
            person = person[1:]

        Xaveco(app.client, ack, say).enviar_xaveco_por_nome(person, message)

    @app.command('/time')
    def what_time_is_it(ack: Ack, say: Say, command: dict):
        Time(app.client, ack, say).time()
