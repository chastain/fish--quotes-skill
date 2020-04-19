from mycroft import MycroftSkill, intent_file_handler


class FishQuotes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('quotes..fish.intent')
    def handle_quotes__fish(self, message):
        self.speak_dialog('quotes..fish')


def create_skill():
    return FishQuotes()

