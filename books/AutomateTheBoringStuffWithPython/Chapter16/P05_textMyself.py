#! python3
# P05_textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

from twilio.rest import Client

# Preset values:
filepath = '/home/jose/PycharmProjects/python-tutorials/books/AutomateTheBoringStuffWithPython/Chapter16/twilio_info'
with open(filepath) as config:
    accountSID, authToken, twilioNumber, myNumber = config.read().splitlines()


def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
    return None
