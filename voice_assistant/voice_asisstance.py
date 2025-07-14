#First step is to import the libraries required 
import pyttsx3 # This converts the text to speech, allowing talk back functitonality
import speech_recognition as sr # this is for listening to voice and converting it to text
import webbrowser # opens web pages
import time
from datetime import datetime # tells date and time

#intialising text to speech engine
#engine = pyttsx3.init(driverName='sapi5') 
#I had to specify the driver name because of the first test no sound was heard

#Function that enables the assistant to speak

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.2)
#if running in spyder ide, restart kernel after first run whenever voice is not audible

#listens to speech and converts to text    
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Assistant is listening...")
        # this handles any background noice
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        print("Recording....")
        query = r.recognize_google(audio)
        print (f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError():
        print("Speech not understood.")
        return ""
    except sr.RequestError:
        print("Sorry. Service not available")
        return""
        
    #what the function abouve does: creates a recogniser object, uses systems microphone to record audio, sends it to googles speech recognition services and returns it in lowercase
 

while True:
    command =  listen() 
    #continues program if user has not spoken
    if command == "":
        continue
    #stops the loop
    if "exit" in command or "stop" in command:
        speak("Goodbye")
        break 
    if "hello" in command:
        speak("Hello. How can i help you today?")
    elif "time" in command:
        date = datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {date}")
        
    elif "who are you" in command or "what is your name" in command:
        speak(" I am your Python voice assistant")

    elif "search for" in command:
        query = command.replace("search for", "")
        link = f"https:/www.google.com/search?q={query}"
        webbrowser.open(link)
        speak(f"This is what i found for {query}")
    else:
        speak("Sorry. Command not understood")
