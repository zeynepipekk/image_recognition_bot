from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X:  380 Y: 400 RGB: (161, 166, 232)
#Tile 2 Position: X:  542 Y: 400 RGB: (  0,   0,   0)
#Tile 3 Position: X:  703 Y: 400 RGB: (156, 162, 231)
#Tile 4 Position: X:  813 Y: 400 RGB: (164, 169, 232)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(380, 400)[0] == 0:
        click(380, 400)
    if pyautogui.pixel(542, 400)[0] == 0:
        click(542, 400)
    if pyautogui.pixel(703, 400)[0] == 0:
        click(703, 400)
    if pyautogui.pixel(813, 400)[0] == 0:
        click(813, 400)
