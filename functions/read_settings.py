import time
import json
import variables.general_names as general_names
from utilities.open_application import openApplication
from functions.check_settings_open import checkSettingsOpen
from utilities.capture_screen import captureScreen
import variables.delay_times as delay_times
import variables.general_names as general_names
from functions.read_settings_general import readSettingsGeneral
from functions.check_settings_open import openSettings

def readSettings():
    openApplication(general_names.application_name)
    time.sleep(delay_times.after_application_open)
    image = captureScreen()
    time.sleep(delay_times.after_screen_capture)

    # Check if settings is open
    if checkSettingsOpen(image):
        print("Settings is open")
    else:
        print("Settings is not open")
        openSettings()

    # Opening the file to write the settings
    file_path = str(general_names.files_path_name) + str(general_names.settings_file_name)
    settings_file = open(file_path, "w")

    settings_file.write(readSettingsGeneral())

    settings_file.close()