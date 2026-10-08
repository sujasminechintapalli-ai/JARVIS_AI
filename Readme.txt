# Jarvis - Simple Python Voice Assistant

A small voice assistant inspired by Iron Man's J.A.R.V.I.S. You talk to it through your microphone, and it answers out loud and on screen.

## Features

Say any of these commands:

| Command | What Jarvis does |
|---|---|
| "hello" | Greets you |
| "what time is it" | Tells you the current time |
| "what is the date" / "today" | Tells you today's date |
| "open YouTube" | Opens YouTube in your browser |
| "open Google" | Opens Google in your browser |
| "search python tutorials" | Searches Google for whatever follows the word "search" |
| "tell me a joke" | Tells a random programmer joke |
| "bye" / "exit" / "quit" | Closes Jarvis |

## Requirements

- Windows with a working microphone and speakers
- **Python 3.13** (PyAudio does not install on Python 3.14 yet)
- An internet connection (speech recognition uses Google's online service)

## Installation

1. Install Python 3.13 from https://www.python.org/downloads/ (tick "Add python.exe to PATH").
2. Open Command Prompt and go to the project folder:
   ```
   cd path\to\your\jarvis\folder
   ```
3. (Recommended) Create and activate a virtual environment:
   ```
   py -3.13 -m venv jarvis_env
   jarvis_env\Scripts\activate
   ```
4. Install the libraries:
   ```
   pip install pyttsx3 SpeechRecognition pyaudio
   ```

## Running Jarvis

```
py -3.13 jarvis.py
```

Wait for "Listening..." and then speak. Say **bye** to stop.

### Running in VS Code

1. Open the project folder in VS Code.
2. Press `Ctrl+Shift+P`, choose **Python: Select Interpreter**, and pick Python 3.13 (or `jarvis_env`).
3. If VS Code still uses 3.14, run it from the terminal with `py -3.13 jarvis.py`.

## How it works

- `listen()` records audio from the microphone and converts it to text using `SpeechRecognition`.
- `handle()` checks the text for known words and decides what to do.
- `speak()` prints the reply and says it out loud using `pyttsx3`. It creates a new speech engine each time, because reusing one can make the voice go silent on Windows.

## Adding your own commands

Open `jarvis.py` and add a new block inside `handle()`:

```python
elif "weather" in command:
    speak("Opening the weather for you")
    webbrowser.open("https://www.google.com/search?q=weather")
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `pip install pyaudio` fails | You are probably on Python 3.14. Use Python 3.13. |
| `No module named ...` | VS Code is using a different Python. Select 3.13, or run `py -3.13 jarvis.py`. |
| Jarvis does not hear you | Check your default microphone and allow microphone access in Windows Settings > Privacy & security > Microphone. |
| "I cannot reach the speech service" | Check your internet connection. |
| Jarvis is silent | Check your volume and the selected speakers in Windows. |
| Jarvis says "I don't know that command" | Speak clearly, or add the command to `handle()`. |

## Libraries used

- [pyttsx3](https://pypi.org/project/pyttsx3/) - text to speech
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - speech to text
- [PyAudio](https://pypi.org/project/PyAudio/) - microphone access
- `datetime`, `random`, `webbrowser` - built into Python