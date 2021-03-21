from typing import Optional

from slack_bolt import Ack, Say
from slack_sdk import WebClient


class SlackFeatures:
    def __init__(self, client: WebClient, ack: Optional[Ack] = None, say: Optional[Say] = None):
        self._client = client
        self._ack = ack
        self._say = say
