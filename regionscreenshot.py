import pyautogui

im1 = pyautogui.screenshot(region=(495, 300, 907, 638))
im1.save(r"./savedimage.png")
