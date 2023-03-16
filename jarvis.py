import pyttsx3
import datetime
import speech_recognition as speech
import webbrowser as wb
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else: 
        speak("Good Evening!")
    speak("Hi Yeear Ahmed Sir.I'm David. How may i help you")

def takeCommand(): #pip install pyaudio
    r = speech.Recognizer()
    with speech.Microphone() as source: 
        print("Sir i'm listening. You can as well speak")
        r.pause_threshold = 1  #You can go to definition to consider audio energy
        audio = r.listen(source)

    try:
        print("I'm tryna comprehend")
        a = r.recognize_google(audio, language ='en-in')
        print(f"User has said: {a}\n")
    except Exception as e:
        print("Could you please repeat or say that again..")
        return "None"
    return a

# def sendEmail(to, content):    #uncomment and put the info if you wanna send email through David AI
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('sendemail@gmail.com', to, content)
#     server.close()


    

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "open youtube" in query: #Say open youtube
            wb.open("youtube.com")
        elif "open google" in query: #Say open google
            wb.open("google.com")
        elif "the time" in query: #Say the time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Yeear Ahmed Sir. It is currently {strTime}. I repeat it's {strTime}")
        elif "open vs code" in query: #Say open V S Code
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "open game" in query: #Say open game
            valo = "E:/Valorant/Riot Games/Riot Client"
            os.startfile(valo)
        elif "open chat" in query: #Say "open chat" to open chatGPT
            wb.open("https://chat.openai.com/chat")

    

        
        
        # elif 'Run email' in query:
        #     try:
        #         speak("Sir what would you like to say..")
        #         content = takeCommand()
        #         to = "youremail@gmail.com"
        #         sendEmail(to, content)
        #         speak("Done sir! Your email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("I'm genuinely apologizing to you sir! Couldn't send the email")

       

