from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    try:
        pyautogui.locateOnScreen('stickman.png', region=(1300, 70, 500, 650), grayscale=True, confidence=0.8)
        print("I can see it")
    except pyautogui.ImageNotFoundException:
        print("I am unable to see it")
    time.sleep(0.5)
