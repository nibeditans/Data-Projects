import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker1.1. Created by NS!")

    engine = pyttsx3.init()

    while True:
        x = input("Enter what do you want me to speak: ")
        if x == "s":
            break

        engine.say(x)
        engine.runAndWait()
        
