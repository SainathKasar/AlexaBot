import os
import time as t
import random
import pygame
import webbrowser as wb
import pywhatkit
import pyttsx3  # module used to text2speak
import speech_recognition as sr  # module audio inputs
import datetime  # handling with date and time issues
import cv2 as cv
import wikipedia
from email import message
from asyncio.windows_events import NULL
from cgi import print_arguments
from logging import exception
from re import T
from pygame import mixer
from fileinput import filename
from importlib.resources import path
from msilib.schema import Directory

engine = pyttsx3.init('sapi5')
# Constructor used to initiate sapi5 function in already installed in windows
voices = engine.getProperty('voices')
# It has the list of inbuild voices
engine.setProperty("voice", voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.setProperty("rate", 150)

def wishme():
    # it focus on hours(24 hour clock)
    time = int(datetime.datetime.now().hour)
    if(time > 0 and time < 12):
        speak("good morning buddy!")
    elif(time >= 12 and time < 16):
        speak("good afternoon buddy!")
    elif(time >= 16 and time < 22):
        speak("good evening buddy!")
    else:
        speak("good night buddy!")
    t.sleep(1)
    speak("I hope you are doing will buddy")
    speak("please tell me how can i help you!")

def audio_input():  # it takes microphone input from user
    mic = sr.Recognizer()
    # this will make our microphone as source of input
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        mic.energy_threshold = 1000
        mic.pause_threshold = 1
        # it is 1 sec gap, so that while it will not take any half input if i took gap to speak
        # mic.adjust_for_ambient_noise(source,duration="0.2")
        audio = mic.listen(source)
    try:
        print("Implementing...")
        task = mic.recognize_google(audio, language="en-IN")
        print(task)
        if(len(task) == 0):
            audio_input()
        else:
            return task
    except:
        speak(" ")
        return "None"
    return task

if __name__ == '__main__':
    while True:
        ok_alexa = audio_input().lower()
        if ("ok" and "alexa" in ok_alexa):
            wishme()
            while True:
                audio = audio_input()
                my_task = audio.lower()
                if(my_task == "None"):
                    continue

                if('please' or 'alexa' in my_task):

                    if ('youtube' in my_task):
                        speak("opening youtube")
                        wb.open("https://www.youtube.com")

                    if ('google' in my_task):
                        speak("what do you want to search")
                        search = audio_input().lower()
                        search="ghal sainik ki atmagatha in hindi"
                        search=search.replace(" ","+")
                        speak("opening google")
                        if ("nothing" or"None" in search):
                            wb.open("https://www.google.com")
                        else:
                            wb.open("https://www.google.com/search?q="+search)

                    if('play' and ('song' or 'music') in my_task):
                        speak("I will play the song of my choice")
                        if('play' or 'song' or 'next' in my_task):
                            # music_list=os.listdir("F:\\Songs")
                            song = os.listdir("F:\\Songs")
                            mixer.init()
                            os.chdir("F:\\Songs")
                            s = 0
                            speak("say pause to Pause the music")
                            speak("say resume to Resume the music")
                            speak("say quit or exit to change the task")
                            # Remember to give 2 backward slashes for file directory
                            while True:
                                mixer.music.load(song[s])
                                mixer.music.play()
                                i = audio_input().lower()
                                if("pause" in i):
                                    mixer.music.pause()
                                elif("resume" in i):
                                    mixer.music.unpause()
                                elif("quit" or "exit" in i):
                                    mixer.music.pause()
                                    break
                                else:
                                    s += 1
                                    t.sleep(30)
                                    continue
                        os.chdir("F:\programming\python\First_AI")

                    if("send" and "message" in my_task):
                        phonelist = {
                            "rohan": "+917741915787", "father": "+919822771729", 'darshan': "+919284855124"}
                        speak("to whom you want to send message")
                        inp = audio_input().lower()
                        if (inp in phonelist):
                            speak("please tell the message you want to send")
                            message = audio_input()
                            pywhatkit.sendwhatmsg_instantly(
                                phonelist[inp], message)
                            t.sleep(20)
                            os.system("taskill /F /IM chrome.exe /T")
                        else:
                            speak("I am unable to send message")
                            t.sleep(1)

                    if("photo" and "take" in my_task):
                        video = cv.VideoCapture(0)
                        speak("say cheeeeeeeeese")
                        while True:
                            ret, frame = video.read()
                            cv.imshow("Web Cam1", frame)
                            click = audio_input().lower()
                            if (click == "alexa" or click == "smile" or click == "cheese"):
                                if ret:  # ret==true of frame is captured properly
                                    speak("please tell me filename")
                                    fileName = audio_input().lower()+".png"
                                    os.chdir("F:\programming\python\First_AI\AI_photos")
                                    cv.imwrite(fileName, frame)
                                video.release()
                                cv.destroyAllWindows()
                                break
                            else:
                                speak("I am unable to take picture")
                        speak("Image saved successfully!")

                    if ("tell" and "information" in my_task):
                        speak("what information you want")
                        info = audio_input().lower()
                        try:
                            full_info = wikipedia.summary(info, sentences=2)
                            print(full_info)
                            speak(full_info)
                            speak("Extracting was successfull")
                            speak("do you want more information")
                            yeah = audio_input().lower()
                            if("yes" in yeah):
                                wb.open("https://www.google.com/search?q"+info)
                            else:
                                continue
                        except:
                            speak("I was unable to get information")

                    if("open" and "folder" in my_task):
                        if("programming" in my_task):
                            if("c" in my_task):
                                os.startfile("F:\\programming\\c")
                            if("cpp" in my_task):
                                os.startfile("F:\\programming\\c++")
                            if("python" in my_task):
                                os.startfile("F:\\programming\\python")
                            if("web" or "development" in my_task):
                                os.startfile(
                                    "F:\\programming\\web_development")
                            else:
                                os.startfile("F:\\programming")
                        elif("movie" or "movies" or "flim" in my_task):
                            os.startfile("F:\\movies")
                        elif("song" or "songs" in my_task):
                            os.startfile("F:\\Songs")
                        elif("recycle" or "bin" in my_task):
                            os.startfile("F:\\$RECYCLE.BIN")
                        elif("photo" or "photos" in my_task):
                            os.startfile("F:\\Photos")
                        else:
                            speak("i was unable to open folder")

                    else:
                        continue

                elif("sorry" in my_task):
                    speak("now I am forgiving you")
                    speak("but what is task for me")

                elif("thankyou" in my_task):
                    speak("It's my pleasure to work with you")
                    speak("what is our next task")

                elif ('goodbye' in my_task):
                    speak("Good bye!")
                    os.system("shutdown /s /t 1")
                    
                elif('restart' in my_task):
                    speak("we will me in a while")
                    os.system("shutdown /r /t 1")

                elif(('please' and 'alexa' not in my_task) and (len(my_task) > 5)):
                    speak("you should start with")
                    print("please alexa")
                    speak("please alexa before giving the task")
                    speak("Because I am not your servant buddy")

        else:
            continue
