recognizer = sr.Recognizer()
def record_audio():
    with Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio
def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")
if name is "main__":
    audio = record_audio()
    recognize_speech(audio)