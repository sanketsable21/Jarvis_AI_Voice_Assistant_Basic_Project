import sys
sys.path.append('C:\Jarvis-main')
from Speak import speak
import datetime

def greet_me():
    hour = int(datetime.datetime.now().hour)

    if hour>=3 and hour<=12:
        reply = ("Good Morning Sir..., How may I help you?")
    elif hour>12 and hour<=17:
        reply = ("Good Afternoon Sir..., How may I help you?")
    else:
        reply = ("Good Evening Sir..., How may I help you?")
    
    speak(reply)
#     speak("I'm Jarvis, I'm Ready To Assist You Sir")
# greet_me()
