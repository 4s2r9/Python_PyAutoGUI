import pyautogui
import ctypes
import time

print(pyautogui.size())


while True:

    if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
        pyautogui.hotkey("alt", "h")
        pyautogui.write("arigatougozaimasita")
        pyautogui.press("enter")
        pyautogui.hotkey("ctrl", "enter")
        pyautogui.hotkey("alt", "q")
        pyautogui.moveTo(950, 475)
        time.sleep(3)
        pyautogui.click()
        break
