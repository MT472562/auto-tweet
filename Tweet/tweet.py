import json
import webbrowser
import urllib.parse
import time
import pyautogui
import platform

def os():
    os_name = platform.system()
    return os_name

def tweet_data():
    f = open('tweet_text.txt', 'r')
    text = f.read()
    count=len(text)
    
    json_open = open('./code.json', 'r')
    code = json.load(json_open)
    
    if count == 0:
        status_msg = code["1"]
        status = False
    elif count > 140:
        status_msg = code["2"]
        status = False
    elif count > 0 and count < 140:
        status = True
        status_msg =""
    return text , status ,status_msg

def tweet():
    text,status,status_msg = tweet_data()
    text = urllib.parse.quote(text)
    url = "https://twitter.com/intent/tweet?&text="+f"{text}"
    print(text,status_msg,status)
    return url

def web_browser():
    url = tweet()
    webbrowser.open(url)
    time.sleep(2)
    os_name = os()
    if os_name == "Darwin":    
        pyautogui.keyDown('command')
        pyautogui.hotkey('enter')
    else:
        pyautogui.keyDown('ctrl')
        pyautogui.hotkey('enter')
        
web_browser()



