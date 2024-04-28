#Successfully Created A Small Google Assistent
import speech_recognition as sr
import webbrowser as web
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
         
path ="C:/Program Files/Google/Chrome/Application/chrome.exe %s"

r = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()
pass



mic = sr.Microphone(device_index=1)

with mic as source:
    r.adjust_for_ambient_noise(source, duration=1)
    engine.setProperty('rate', 150)
    print("What Should I Open For You ?")
    print("\t\t\t\tSay 'Video' to Search A Video Or 'link' to search a link !")
    engine.say("What Should I open For You, Video or wanna browse somethin ?")
    engine.runAndWait()
    audio = r2.listen(source)
   
   
    if "video" in r1.recognize_google(audio, language='en'):
        r1.adjust_for_ambient_noise(source, duration=1)
        r1 = sr.Recognizer()
        url = 'http://www.youtube.com/results?search_query='
        with sr.Microphone() as source:
            engine.setProperty( "rate", 150)
            print("Search Your Video")
            engine.say("Search your Video")
            engine.runAndWait()
            audio = r1.listen(source, timeout=5)
               
            try:
                get = r1.recognize_google(audio)
                print(get)
                web.get(path).open(url+get)
                print("Opened Successfully")
                engine.say("Opened Successfully")
                engine.runAndWait()
            except:
                print("Unable To understand ")
                pass;
   
    if "search" in r.recognize_google(audio, language='en'):
        r.adjust_for_ambient_noise(source, duration=1)
        r = sr.Recognizer()
        url = 'https://www.google.com/search?q='
        with sr.Microphone() as source:
            engine.setProperty( "rate", 150)
            print("Which Website Link you Want to Open ?")
            engine.say("Which Website Link you Want to Open ?")
            engine.runAndWait()
            audio = r.listen(source, timeout=5)
               
            try:
                get = r.recognize_google(audio)
                print(get)
                web.get(path).open(url+get)
                print("Opened Successfully")
                engine.say("Opened Successfully")
                engine.runAndWait()
            except:
                print("Unable To understand ")
    pass;