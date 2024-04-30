import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print("User:", user_input)
        return user_input.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't request results. Please check your internet connection.")
        return ""

# Define some example functions for task execution
def greet():
    speak("Hello! How can I assist you today?")

def get_time():
    # Add your code to get the current time
    speak("It's currently 3:30 PM.")

def get_weather():
    # Add your code to get the weather information
    speak("The weather is sunny with a temperature of 25 degrees Celsius.")

# Main function to handle user interaction
def main():
    greet()

    while True:
        user_input = recognize_speech()

        if "time" in user_input:
            get_time()
        elif "weather" in user_input:
            get_weather()
        elif "exit" in user_input:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I'm not sure how to help with that.")

if __name__ == "__main__":
    main()
