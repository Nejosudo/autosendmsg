import pyautogui
import time

def sendMessage(msg, count):
    #print('recibido')
    time.sleep(5)
    #print("enviando")
    c = count
    for _ in range(c):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
        time.sleep(0.5)
    #print("fin")