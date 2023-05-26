# Capture screen window using opencv 

import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import pytesseract

try:
    # window_name = "VALORANT"
    window_name = "valorant_setting_1"
    window = gw.getWindowsWithTitle(window_name)[0]
    window.activate()
    image = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
    image.save("screen.png")

    # Use OCR to read the text in the image
    img = cv2.imread("screen.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    img = cv2.medianBlur(img, 3)
    text = pytesseract.image_to_string(img)
    print(text)
    f = open("text.txt", "w")
    f.write(text)
    f.close()

except Exception as e:
    print(e)
    exit(1)