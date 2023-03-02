import pyautogui
import keyboard
import webbrowser

zoomURL = ["zoomURL",
           "zoomURL",
           "zoomURL",
           "zoomURL",
           "zoomURL",
           ]

while True:
    if keyboard.read_key() == "1":
        webbrowser.open(zoomURL[0])
        break
    elif keyboard.read_key() == "2":
        webbrowser.open(zoomURL[1])
        break
    elif keyboard.read_key() == "3":
        webbrowser.open(zoomURL[2])
        break
    elif keyboard.read_key() == "4":
        webbrowser.open(zoomURL[3])
        break
    elif keyboard.read_key() == "5":
        webbrowser.open(zoomURL[4])
        break
    elif keyboard.is_pressed("esc"):  # 強制終了
        break
    elif keyboard.is_pressed("e"):  # zoom退出
        print(pyautogui.size())
        pyautogui.click(1640, 1050, button="right")
        pyautogui.press("h")
        pyautogui.hotkey("alt", "h")  # alt + h でチャットを起動
        pyautogui.write("arigatougozaimasita")  # 入力
        pyautogui.press("enter")
        pyautogui.hotkey("ctrl", "enter")
        pyautogui.hotkey("alt", "q")
        pyautogui.moveTo(950, 475)  # マウスカーソルの位置
        pyautogui.click()
        break
