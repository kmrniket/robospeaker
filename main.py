import os
import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1 created by Niket")

    def speak_it(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


    while True:
        x = input("Enter what you want me to speak\n")
        if x == "q":
            speak_it("Bye Bye my friend")
            break

        speak_it(x)



