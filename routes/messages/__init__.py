import re

from slack_bolt import App


def set_routes(app: App):
    @app.message(re.compile("(hi|hello|hey)"))
    def say_hello_regex(say, context):
        greeting = context['matches'][0]
        say(f"{greeting}, how are you?")

    @app.message(re.compile("(fine)"))
    def say_hello_regex(say, context):
        say(f"Great!")
