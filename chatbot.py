import sys
sys.path.insert(0, './kernel/')
import aiml as aiml
import os

bot=aiml.Kernel()

bot.learn("./memory/alice-aiml/*.aiml")
bot.learn("./memory/file/*.aiml")
bot.learn("./memory/standard/*.aiml")

def test_ai(text):
          return (bot.respond(text))


