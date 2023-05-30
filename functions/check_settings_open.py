import time
import pyautogui as pg
import variables.text_locations as text_locations
import variables.delay_times as delay_times
from utilities.image_and_text import checkText

def checkSettingsOpen(image):
    if checkText(image, text_locations.settings_general_title, "General"):
        return True
    else:
        return False
    

def openSettings():
    pg.sendHotkey("esc")
    time.sleep(delay_times.after_any_click)
    pg.click(text_locations.settings_button)
    time.sleep(delay_times.after_any_click)