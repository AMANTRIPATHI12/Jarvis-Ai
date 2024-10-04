import os
import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 184)

def speak(audio):
    print("    ")
    print(f":{audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()

extracted_time = open('C:\\Aman\\AI\\My Jarvis\\Advance Jarvis\\Data.txt', 'rt')
time = extracted_time.read()
Time = str(time)

delete_time = open("C:\\Aman\\AI\\My Jarvis\\Advance Jarvis\\Data.txt", 'r+')
delete_time.truncate(0)
delete_time.close()

def play_sound(file_path):
    os.startfile(file_path)  # This works on Windows to open the file with the default application

def RingerNow(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("jarvis", "")
    time_now = time_now.replace("set alarm for ", "").replace("set ", "").replace("alarm ", "").replace("for ", "").replace(" and ", ":")

    Alarm_Time = str(time_now)

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")

        if current_time == Alarm_Time:
            speak("Time to Wake Up Sir")
            play_sound("D:\\Aman\\My Jarvis\\Advance Jarvis\\Database\\Sounds\\iron.mp3")

        elif current_time > Alarm_Time:
            break

RingerNow(Time)
