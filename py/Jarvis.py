import speech_recognition as sr
import pyttsx3
import webbrowser
import pyjokes
from datetime import *
# Function to recognize speech
def record():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a song name or command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        data = recognizer.recognize_google(audio)
        print('You said:', data)
        return data.lower()  # Convert to lowercase for easy comparison
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return ""

# Function to respond via text-to-speech
def Read(data):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(data)
    engine.runAndWait()

# Main program
if __name__ == '__main__':

    while True:
        data1 = record()  # Get user input via voice
        
        if 'play song' in data1:  # Check if user said 'play'
            song_name = data1.replace('play', '').strip()  # Extract song name
            Read(f"Playing {song_name} on YouTube.")
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={song_name}")


        elif 'current date' or 'the date' in data1:
            t = datetime.now().strftime('%Y-%m-%d')
            Read(f"The current date is {t}.")

        elif 'current time' or 'the time' in data1:
            t = datetime.now().strftime('%I-%M-%p')
            Read(f'Current Time is {t}')


        elif 'open' in data1:
            web = data1.split('open ')[1]
            url = f'www.{web}.com'
            Read(f"Opening {url}.")
            webbrowser.open_new_tab(url)
            
        elif 'stop' in data1 or 'exit' in data1:  # Exit the program
            Read("Goodbye!")
            break
        
        else:
            Read("I could not understand your command. Please try again.")
