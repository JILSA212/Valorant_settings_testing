import cv2 as cv
import pyautogui as pg
import variables.general_names as general_names

def captureScreen():
    img = pg.screenshot()
    img.save(str(general_names.images_path_name) + str(general_names.image_name))
    img = cv.imread(str(general_names.images_path_name) + str(general_names.image_name))
    return img

def getImage(image_name):
    img = cv.imread(str(general_names.images_path_name) + str(image_name))
    return img