import pyttsx3

text = input("Enter text you wanna listen : ")

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()