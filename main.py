import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    print(command)
    if "open you tube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "play song" in command.lower():
        pywhatkit.playonyt(command.lower())



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    try: 
        audio = r.listen(source, timeout=5)  # Set a reasonable timeout
        print("Recognizing...")
        word = r.recognize_google(audio)
        print(f"You said: {word}")
        speak(word)
        if(word.lower() == "betu"):
            speak("Yes, mumma")
            print("Waiting for command..")
        with sr.Microphone() as source:
            text = r.listen(source, timeout=5)  
            command = r.recognize_google(text)
            process_command(command)

    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


