import pyttsx3
import speech_recognition as sr
from Features import *
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',184)

def speak(audio):
    print("    ")
    print(f":{audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand( ):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.50
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio , language= 'en-in')
            print(f": you said : {query}\n")

        except:
            return ""

        return query.lower()

def TaskExe():
    speak("i am on")
    while True:
        query = TakeCommand()

        if "hey jarvis" in query:
            wishMe()
        
        elif "hi jarvis" in query:
            wishMe()
        
        elif "hello jarvis" in query:
            wishMe()
        
        elif "jarvis" in query:
            wishMe()

        elif 'youtube search' in query:
            YoutubeSearch(query)
            
        elif "i am good how are you" in query:
            speak("i am good as always any task sir")

        elif "take a break" in query:
            speak("ok sir you can call me any time")
            break
        
        elif "bye" in query:
            speak("ok sir bye")
            break

        elif "goodbye" in query:
            speak("ok sir bye")
            break

        elif "good night" in query:
            speak("ok sir bye")
            break

        elif "sayonara" in query:
            speak("ok sir bye")
            break

        elif "bhag yahan se" in query:
            speak("ok sir bye")
            break

        elif "google search" in query:
            Google_search(query)

        elif"set alarm" in query:
            Alarm(query)

        elif 'jarvis download' in query:
            DownloadYouTube()

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("Name of the file")
            Name = TakeCommand()
            speak("taking screenshot")
            screenshot(Name)

        elif "thank you" in query:
            speak("my pleasure sir")

        elif 'dictionary' in query:
            speak("Name of the word")

        elif 'the time' in query:
            time()

        elif 'play music' in query:
            speak("sir tell me the name of the music")
            musicName = TakeCommand()
            music(musicName)
        
        elif "internet is not working" in query:
            speak("Sir i dont know anything")

        elif "why you don't know" in query:
            speak("Because sir...  i am dumb")

        elif "pause" in query:
            keyboard.press("space bar")
        
        elif "play" in query:
            keyboard.press("space bar")

        elif "restart" in query:
            keyboard.press("0")

        elif "mute" in query:
            keyboard.press("m")

        elif "skip" in query:
            keyboard.press("l")

        elif "back" in query:
            keyboard.press("j")
        
        elif "full screen" in query:
            keyboard.press("f")

        elif "normal screen" in query:
            keyboard.press("f")

        elif "open google maps" in query:
            web = "https://www.google.com/maps/@28.5957734,77.0836946,20z"
            query = query.replace("open","")
            query = query.replace("jarvis","")
            webbrowser.open(web)
            speak("opening")

        elif "open new tab" in query:
            query = query.replace("jarvis","")
            keyboard.press_and_release('ctrl + t')
        
        elif "close this tab" in query:
            query = query.replace("jarvis","")
            keyboard.press_and_release('ctrl + w')

        elif "switch" in query:
            query = query.replace("jarvis","")
            keyboard.press_and_release('ctrl + tab')

        elif "open new window" in query:
            query = query.replace("jarvis","")
            keyboard.press_and_release('ctrl + shift + n')

        elif "next window" in query:
            query = query.replace("jarvis","")
            keyboard.press_and_release('alt + tab')

        elif "down" in query:
            pyautogui.press("down")

TaskExe()