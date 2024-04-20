import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)
#print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am your assistant AI,How can I help you")

def takeCommand():
    '''It takes microphone input from user and string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
def SendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ashudidwania1512@gmail.com','Ashu@15122002')
    server.sendmail('ashudidwania1512@gmail.com',to,content)
    server.close()


if __name__=='__main__':
   # speak("Hi,Ashutosh How are you")
   wishme()
   #while True:
   if 1:
       query=takeCommand().lower()
       #logic for executing task based on query
       if 'wikipedia' in query:
           speak("Searching Wikipedia...")
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")

       elif 'open google' in query:
           webbrowser.open("google.com")

      # sites=[["youtube","https://www.youtube.com"],["google","https://www.google.com"],["wikipedia","https://www.wikipedia.com"]]
      # for site in sites:
      # if f"open {site[0]}" in query:
      # speak(f"opening {site[0]} sir...")
      # webbrowser.open(site[1])

       elif 'open music' in query:
           music_dir = 'D:\\music'
           songs=os.listdir(music_dir)     #list all song in music directory.
           os.startfile(os.path.join(music_dir,songs[0]))

       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"the time is:{strTime}")

       elif 'open code' in query:
           codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
           os.startfile(codePath)

       elif 'email to ashu' in query:
           try:
               speak("What should I say")
               content=takeCommand()
               to="a81705351@gmail.com"
               SendEmail(to,content)
               speak("Email Sent")

           except Exception as e:
               print(e)
               speak("Email can't sent")

       










