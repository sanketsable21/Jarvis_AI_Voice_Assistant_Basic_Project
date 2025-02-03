import pyttsx3


def speak(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    # Speak the text
    print(text)
    engine.say(text)
    # Wait until speech is finished
    engine.runAndWait()

# # Example usage:
# speak("Hello Calculator")
