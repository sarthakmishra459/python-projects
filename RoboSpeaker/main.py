
import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")



while(True):
    print("Enter q or Q to exit")
    text = input("Enter the text you want to convert to speech: ")
    if text == "q" or text == "Q":
        break
    speak.Speak(text)

speak.Speak("bye")
# 3-second sleep
# time.sleep(3)

# text2 = text
# speak.Speak(text2)
