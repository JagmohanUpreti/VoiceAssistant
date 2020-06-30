import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import os


engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning! ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening! ")

    speak("I am your Assistant Sir...Please tell me how may I help you")


def takeCommand():
    ''' It takes microphone input from the user and returns string output '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1841
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query


def start():
    ''' Logic for executing tasks based on query '''

    wishMe()
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'youtube' in query:
        webbrowser.open("https://youtube.com")

    elif 'google' in query:
        webbrowser.open("https://google.com")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The time is {strTime}")

    elif 'music' in query:
        music_dir = "F:\\Music"
        songs = os.listdir(music_dir)
        n=random.randint(0,5)
        os.startfile(os.path.join(music_dir, songs[n]))

    elif 'vs code' in query:
        codepath = 'C:\\Users\\JEEVAN UPRETI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(codepath)

    elif 'who are you' in query:
        speak('I am a Desktop Voice Assistant sir')

    elif 'quit' in query:
        print("Switching off...Please wait")
        speak("Switching off...Please wait")
        exit()

    else:
        print("Sorry I can't recognize this... Please Try again...!")
        speak("Sorry I can't recognize this... Please Try again...!")


# GUI Code

from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("   Desktop Voice Assistant")
root.wm_iconbitmap("f:\\Python Project\\title.ico")
root.minsize(500, 500)
root.maxsize(500, 500)


photo=PhotoImage(file="f:\\Python Project\\background.png")

f1 = Frame(root, bg="grey", borderwidth=6)
f1.pack()

l1 = Label(f1, image=photo, padx=200, pady=200)

l1.pack()


b1 = Button(l1, text="Tap to Speak", font="mssansserif 14 bold",
            command=start, padx=12, pady=12)
b1.pack(side="bottom")
b1.place(x=160, y=400)


root.mainloop()
