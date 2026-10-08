import datetime
import random
import webbrowser

import pyttsx3
import speech_recognition as sr

# Setup voice input (microphone)
recognizer = sr.Recognizer()


def speak(text):
    print("Jarvis:", text, flush=True)
    # Create a fresh engine every time. On Windows, reusing one engine
    # often makes pyttsx3 go silent after the first sentence.
    local_engine = pyttsx3.init()
    local_engine.say(text)
    local_engine.runAndWait()
    local_engine.stop()


def listen():
    """Listen to the microphone and return the text you said."""
    with sr.Microphone() as source:
        print("Listening...", flush=True)
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, phrase_time_limit=6)
    try:
        text = recognizer.recognize_google(audio)  # needs internet
        print("You:", text, flush=True)
        return text.lower()
    except sr.UnknownValueError:
        return ""  # could not understand
    except sr.RequestError:
        speak("I cannot reach the speech service. Check your internet.")
        return ""


JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I would tell you a UDP joke, but you might not get it.",
    "Why did the developer go broke? He used up all his cache.",
]


def handle(command):
    if "hello" in command or "hi" in command.split():
        speak("Hello sir, how can I help you today?")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "date" in command or "today" in command:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command.startswith("search "):
        query = command.replace("search ", "", 1)
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "joke" in command:
        speak(random.choice(JOKES))

    elif "exit" in command or "quit" in command or "bye" in command:
        speak("Goodbye sir. Have a great day!")
        return False

    else:
        speak("Sorry, I don't know that command yet.")

    return True


def main():
    print("(say 'bye' to exit)", flush=True)
    speak("Hello ma'am or sir, how can I help you?")
    running = True
    while running:
        command = listen()
        if command:
            running = handle(command)


if __name__ == "__main__":
    main()