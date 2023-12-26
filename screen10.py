import pyautogui
import time

def take_screenshot():
    screen_width, screen_height = pyautogui.size()

    screenshot = pyautogui.screenshot()
    screenshot.save(f"screenshot_{int(time.time())}.png")

while True:
    take_screenshot()
    time.sleep(10)