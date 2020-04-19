from mycroft import MycroftSkill, intent_file_handler
import random

class FishQuotes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('quotes..fish.intent')
    def handle_quotes__fish(self, message):
        self.speak_dialog('quotes..fish')

        fishing_quotes = [
            ("There is a fine line between fishing and just standing on the shore like an idiot", "Steven Wright"),
            ("As no man is born an artist, so no man is born an angler", "Izaak Walton, The Compleat Angler"),
            ("Many men go fishing all of their lives without knowing that it is not fish they are after", "Henry David Thoreau"),
            ("Be patient and calmfor no one can catch fish in anger", "Herbert Hoover"),
            ("If I fished only to capture fish, my fishing trips would have ended long ago", "Zane Grey"),
            ("If fishing is a religion, fly fishing is high church", "Tom Brokaw"),
            ("Do not tell fish stories where the people know you. Particularly, don't tell them where they know the fish", "Mark Twain"),
            ("There's no taking trout with dry breeches", "Cervantes"),
            ("It has always been my private conviction that any man who pits his intelligence against a fish and loses has it coming", "John Steinbeck"),
            ("Somebody just back of you while you are fishing is as bad as someone looking over your shoulder while you write a letter to your girl", "Ernest Hemingway")
        ]

        fishing_quote = random.choice(fishing_quotes)

        self.speak_dialog(fishing_quote[0])
        self.speak_dialog(fishing_quote[1])

def create_skill():
    return FishQuotes()

