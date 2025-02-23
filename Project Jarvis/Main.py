import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
import os
from gtts import gTTS
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Use your api key here"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
     tts = gTTS(text)
     tts.save('temp.mp3')

     # Initialize pygame mixer
     pygame.mixer.init()

     # Load the MP3 file
     pygame.mixer.music.load("temp.mp3")  # Replace with your MP3 file path

     # Play the MP3 file
     pygame.mixer.music.play()

     # Keep the program running until the music stops
     while pygame.mixer.music.get_busy():
        continue  # Keeps checking if the music is still playing
     pygame.mixer.music.unload()
     os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(
    api_key = "Use your api key here"
)

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis who performs general tasks asked by the user like alexa and google assistant."},
        {"role": "user", "content": command}
    ]
)
    return(completion.choices[0].message)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            for article in articles[:5]:  # Print first 5 articles
                speak(f"Title: {article['title']}")
    # else:
    #     # Let opneAI handle the request
    #     output = aiProcess(command)
    #     speak(output)
        


if __name__ == "__main__":
    speak("Initializing Jarvis")
    speak("Good morning shreyans, How are you doing today")

    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
    
