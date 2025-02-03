# import sys
# sys.path.append('C:\Jarvis-main')
import keyboard

from Speak import speak
from Listen import mic_execution
from GreetMe import greet_me
import wikipedia
import webbrowser
import os
import datetime
from time import sleep
import keyword
print(">> Starting The Jarvis : Wait For Some Seconds.")


greet_me()

def main_execution():
    while True:
        query = mic_execution()
        # Data = input("\nYou : ")
        query = str(query).lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            pass

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            pass

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            pass

        elif 'open google' in query:
            webbrowser.open("google.com")
            pass

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            pass



        # elif 'play music' in query:
        #     music_dir = '"C:\Users\sanke\Music\Ganpati bappa songs  top ganpati songs  Lord Ganesha songs.mp3"'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))
        #     pass

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            pass


        elif 'open' in query:
            query = query.replace("open","")
            speak(f"Opening {query}")
            keyboard.press_and_release('win')
            sleep(1)
            keyboard.write(query)
            sleep(1)
            keyboard.press_and_release('enter')
            sleep(1)
            speak(f"{query} now open")
            pass

        elif 'turn off' in query:
            os.system('shutdown /s /t 1')
            pass

        elif len(query) < 2:
            pass
        elif 'go to sleep' in query:
            break


main_execution()
