import requests
import json
import win32com.client as wincom
import time

city = input("Enter the name of city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=e55844080979444bb9460608232506&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(wdic["current"]["temp_c"])
speak = wincom.Dispatch("SAPI.SpVoice")
text = w
speak.Speak(text)

# 3-second sleep
time.sleep(3)

text2 = text
speak.Speak(text2)
