from datetime import datetime

from features import SlackFeatures


class Time(SlackFeatures):
    def time(self):
        self._ack(f'agora são {datetime.now().isoformat()}')
