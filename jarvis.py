import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
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

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=80ipxC2AZfk&list=RDMM80ipxC2AZfk&start_radio=1")
        elif 'open it mate pakistan' in query:
            webbrowser.open("https://www.youtube.com/@itmatepakistan")
        elif 'open cloudinary' in query:
            webbrowser.open("https://console.cloudinary.com/console/c-a259bc088d47c24f9ea30eb528eff7/media_library/homepage")
        elif 'open cloudinary documentation' in query:
            webbrowser.open("https://cloudinary.com/documentation")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open freepik' in query:
            webbrowser.open("https://www.freepik.com/")
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open surah mulk' in query:
            webbrowser.open("https://www.youtube.com/watch?v=JwXN2fnc8Uk&t=184s&pp=ygUKc3VyYWggbXVsaw%3D%3D")
        elif 'open surah waqiah' in query:
            webbrowser.open("https://www.youtube.com/watch?v=N78PGdl2-Wo&pp=ygUMc3VyYWggd2FxaWFo")
        elif 'open surah yaseen' in query:
            webbrowser.open("https://www.youtube.com/watch?v=65KT3SJIN2s&pp=ygUMc3VyYWggeWFzZWVu")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

       
            
        elif 'open photo album project' in query:
            codePath = "E:\data\MAIN PROJECT SOURCE\Hackathon\hackathon zero\hackathon_zero"
            os.startfile(codePath)
        elif 'open FX project' in query:
            codePath = "E:\data\MAIN PROJECT SOURCE\ fx"
            os.startfile(codePath)
        elif 'open code book' in query:
            codePath = "E:\data\codes book"
            os.startfile(codePath)
        elif 'open photoshop' in query:
            codePath = "C:\Program Files\Adobe\Adobe Photoshop 2020\Photoshop.exe"
            os.startfile(codePath)
        elif 'open Adobe Illustrator' in query:
            codePath = "C:\Program Files\Adobe\Adobe Illustrator 2020\Support Files\Contents\Windows\Illustrator.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
