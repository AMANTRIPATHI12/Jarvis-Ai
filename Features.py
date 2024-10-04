import wikipedia as googlescrap
import pywhatkit
import pyautogui
import os
import pyttsx3 , time
import datetime
import webbrowser as web
import webbrowser
import os
import psutil
import pyjokes , random
#from PyDictionary import PyDictionary as Diction

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    print("    ")
    print(f":{audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hey sir its jarvis , How are you")

def Google_search(term):
    Query = str(term)

    Query = Query.replace("google","")
    Query = Query.replace("jarvis","")
    Query = Query.replace("search","")
    Query = Query.replace("what is","")
    Query = Query.replace("what do you mean by","")
    Query = Query.replace("where is","")
    Query = Query.replace("who is","")
    Query = Query.replace("when was the","")
    Query = Query.replace("how to","")

    pywhatkit.search(Query)
    speak("this is what i found sir on web")

    web = (f"https://www.google.com/search?q={Query}&sxsrf=ALeKk02OFGnLpzd-0XEHxB2dWLZkfw0wXg:1620569929307&source=lnms&tbm=isch&sa=X&ved=2ahUKEwir6eC35bzwAhVj4jgGHW-uDUgQ_AUoAXoECAEQAw&cshid=1620570188020853&biw=1366&bih=625")
    webbrowser.open(web)

    try:
        result = googlescrap.summary(Query , 2)
        speak(result)

    except:
        speak("No speakable Data is available")

def YoutubeSearch(term):
    result = 'https://www.youtube.com/results?search_query='+ term
    web.open(result)
    speak("This is what i found sir")
    pywhatkit.playonyt(term)
    speak("This may also help you sir")

def Alarm(query):
    TimeHere=  open('C:\\Aman\\AI\\My Jarvis\\Advance Jarvis\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Aman\\AI\\My Jarvis\\Advance Jarvis\\Database\\Extra Prog\\Alarm.py")

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep
    sleep(1)
    click(x=981,y=50)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 
    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('D:\\Aman\\My Jarvis\\Advance Jarvis\\Database\\Youtube Downloaded videos\\')
    Download(Link)
    speak("Done Sir,I Have Downloaded The Video.")
    speak("Here it is.")
    os.startfile('D:\\Aman\\My Jarvis\\Advance Jarvis\\Database\\Youtube Downloaded videos\\')

def screenshot(Name):
    img = pyautogui.screenshot()
    img.save(f'D:/Aman/My Jarvis/Advance Jarvis/Database/ScreenShot/{Name}.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
    
def joke():
    a = (pyjokes.get_jokes())
    b = random.choice(a)
    speak(b)

def time():
    strTime = datetime.datetime.now().strftime("%I:%M:%p")
    speak(f'Sir, the time is {strTime}')

def sutdown():
    os.system('shutdown /p /f')

def music(musicName):
        default = ["Spider-Man: Far From Home Soundtrack - Back in Black by AC/DC","Charlie Puth - Attention" , "shape of you" , ""]
        defo = random.choice(default)
        if musicName == "":
            pywhatkit.playonyt(defo)
        else:
            pywhatkit.playonyt(musicName)
        speak("your song has been started enjoy sir")



# Alarm("set alarm for 00 and 30")
