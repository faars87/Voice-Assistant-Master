import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
query = re.sub(r'[^\w\s]', '', query) 
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':

    speak("Amigo assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak("Fetching weather details...")
            webbrowser.open("https://www.weather.com")

            speak(results)
command_map = {
        'open youtube': lambda: webbrowser.open("youtube.com"),
        'open google': lambda: webbrowser.open("google.com"),
        'open github': lambda: webbrowser.open("github.com"),
        'open stackoverflow': lambda: webbrowser.open("stackoverflow.com"),
        'open spotify': lambda: webbrowser.open("spotify.com"),
        'play music': lambda: webbrowser.open("spotify.com"),
         'open whatsapp': lambda: os.startfile("C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"),
       'local disk d': lambda: webbrowser.open("D://"),
       'local disk c': lambda: webbrowser.open("C://"),
        'local disk e': lambda: webbrowser.open("E://"),
       'weather': lambda: webbrowser.open("https://www.weather.com"),
       'lock screen': lambda: os.system("rundll32.exe user32.dll,LockWorkStation")
}
for key in command_map:
       if key in query:
        speak(f"Executing {key}")
        command_map[key]()
        break