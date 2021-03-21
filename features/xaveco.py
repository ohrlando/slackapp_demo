from typing import Optional

from qdict import find

from features import SlackFeatures


class Xaveco(SlackFeatures):
    """
    Manda xaveco para usuários
    """
    
    def say(self, text: str, channel: str):
        if self._say:
            self._say(text, channel=channel)
        else:
            self._client.chat_postMessage(
                channel=channel,
                text=text
            )

    def enviar_xaveco_por_nome(self, person, message: Optional[str]):
        try:
            user_list = self._client.users_list().data
        except Exception as e:
            print(f'erro ao obter usuários: {e}')
        else:
            users = list(find(user_list.get('members'), {'name': person}))
            if users:
                self.enviar_xaveco(users[0], message)
            else:
                self._ack('Não achei o amor da sua vida "/')

    def enviar_xaveco(self, person_id: str, message: Optional[str]):
        self.say(f'você recebeu um xaveco anônimo: {message}', channel=person_id)
