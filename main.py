import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter the name of the city:::::\n")

url = f"https://api.weatherapi.com/v1/current.json?key=51b1ce1fe40b40c2a84170827230505&q={city}"

r = requests.get(url)
speak.Speak("whole report is given below")
print(r.text)
wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])
print(f" \n\n The current weather in {city} is {w} degrees")
say = (f"but the current weather in {city} is {w} degrees")
speak.Speak(say)