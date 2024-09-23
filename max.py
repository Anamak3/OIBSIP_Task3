import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import wikipedia

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry, I didn't catch that. Could you repeat?")
            return "None"
        return query

# Function to greet the user
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Max, your virtual assistant. How can I assist you today?")

# Function to respond to queries
def respond_to_query(query):
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError:
            speak("Multiple results found. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, no information found on Wikipedia.")

    elif 'who is the president of india' in query:
        speak("The President of India is Droupadi Murmu, as of 2023.")

    elif 'who is the prime minister of india' in query:
        speak("The Prime Minister of India is Narendra Modi.")

    elif 'who is the current captain of the indian cricket team' in query:
        speak("The current captain of the Indian cricket team is Rohit Sharma, as of 2023.")

    elif 'what day is today' in query:
        today = datetime.datetime.now().strftime("%A")
        speak(f"Today is {today}.")

    elif 'what is the capital of india' in query:
        speak("The capital of India is New Delhi.")

    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")

    elif 'open code' in query:
        code_path = "C:\\path\\to\\your\\IDE\\Code.exe"  # Update with your code editor path
        speak("Opening Visual Studio Code")
        os.startfile(code_path)

    elif 'bye' in query or 'exit' in query:
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("Sorry, I don't know the answer to that. Please try asking something else.")

    return True

# Main function with basic tasks
def max_assistant():
    greet_user()
    while True:
        query = take_command().lower()
        if query == "none":
            continue
        if not respond_to_query(query):
            break

# Run Max
if __name__ == "__main__":
    max_assistant()
