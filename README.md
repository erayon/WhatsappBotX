# Whatsaap chat bot using selenium

Selenium is a tool to test your web application. You can do this in various ways, for instance

1. Permit it to tap on buttons
2. Enter content in structures
3. Skim your site to check whether everything is "OK" and so on.


# Prerequisites

1. Python3.2 or higher (https://www.python.org/downloads/)
2. firefox (https://www.mozilla.org/en-US/firefox/new/)
3. selenium (http://selenium-python.readthedocs.io/)
4. aiml (https://pypi.python.org/pypi/python-aiml/0.9.0)


```
apt-get install firefox
pip install selenium
pip install aiml
```

# installation and running bot
```
# Clone the github repository
git clone https://github.com/erayon/WhatsappBotX.git
cd WhatsaapBotX
python WbotX.py
```

## Note
- Emoji,photo,gif,videos,attachment are not supported
- One to One client chat 
- For force turned off : keyword "shutdown" from client side
- Time out session of 20sec if no reply from client side
- one can change time out session under WbotX.py change waiting=20 to any number

