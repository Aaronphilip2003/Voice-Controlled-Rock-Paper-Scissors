import pyaudio
import speech_recognition as sr
import pyttsx3
import random


# Making the computer Speak
engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Speech Recognition

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising...........")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except:
        print("Please Say that again.......")
        return "None"
    return query


if __name__=="__main__":

    while True:

        query=takeCommand().lower()
        comp = random.randint(1, 3)
        player = 0
        if query == "rock":
            player = 1
        elif query == "paper":
            player = 2
        elif query == "scissors":
            player = 3

        if player == 1:
            if comp == 1:
                speak("TIE! The computer chose Rock")
                print("TIE! The computer chose Rock")
            elif comp == 2:
                speak("You Lost! The computer chose Paper")
                print("You Lost! The computer chose Paper")
            elif comp == 3:
                speak("You Won! The computer chose Scissors")
                print("You Won! The computer chose Scissors")

        if player == 2:
            if comp == 1:
                speak("You Won! The computer chose Rock")
                print("You Won! The computer chose Rock")
            elif comp == 2:
                speak("Tie! The computer chose Paper")
                print("Tie! The computer chose Paper")
            elif comp == 3:
                speak("You Lost! The computer chose Scissors")
                print("You Lost! The computer chose Scissors")

        if player == 3:
            if comp == 1:
                speak("You Lost! The computer chose Rock")
                print("You Lost! The computer chose Rock")
            elif comp == 2:
                speak("You Won! The computer chose Paper")
                print("You Won! The computer chose Paper")
            elif comp == 3:
                speak("TIE! The computer chose Scissors")
                print("TIE! The computer chose Scissors")





