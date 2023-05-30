import time
import json
import pyautogui as pg
import variables.text_locations as text_locations
import variables.delay_times as delay_times
import variables.text_strings as text_strings
from utilities.image_and_text import checkText
from utilities.image_and_text import readText
from utilities.image_and_text import compareImages
from utilities.image_and_text import calibrateDisplay
from utilities.capture_screen import captureScreen

def readSettingsGeneral():
    new_size = pg.size()
    general_settings = {}

    # Open General Settings
    pg.click(calibrateDisplay(new_size, text_locations.settings_general_click))
    time.sleep(delay_times.after_click)

    # If it's not on top, get it to the top
    time.sleep(delay_times.random_delay)
    pg.scroll(-1000)

    # Capture the screen
    image = captureScreen()

    # Read General Settings
    
    # Read Text Language
    if(checkText(image, calibrateDisplay(text_locations.general_text_language), text_strings.general_text_langugage)):
        print("General Settings is open")
        general_settings["General Settings"] = readText(image, calibrateDisplay(text_locations.general_text_language_value))
    else:
        print("General - Text Language not found")
    time.sleep(delay_times.after_reading_values)

    # Read Enemy Color
    if(checkText(image, calibrateDisplay(text_locations.general_enemy_color), text_strings.general_enemy_color)):
        print("Enemy Color is open")
        general_settings["Enemy Color"] = readText(image, calibrateDisplay(text_locations.general_enemy_color_value))
    else:
        print("General - Enemy Color not found")
    time.sleep(delay_times.after_reading_values)

    # Read Sensitivity: Aim
    if(checkText(image, calibrateDisplay(text_locations.general_sensitivity_aim), text_strings.general_sensitivity_aim)):
        print("Sensitivity: Aim is open")
        general_settings["Sensitivity: Aim"] = readText(image, calibrateDisplay(text_locations.general_sensitivity_aim_value))
    else:
        print("General - Sensitivity: Aim not found")
    time.sleep(delay_times.after_reading_values)

    # Read Scoped Sensitivity Multiplier
    if(checkText(image, calibrateDisplay(text_locations.general_sensitivity_scoped), text_strings.general_sensitivity_scoped)):
        print("Scoped Sensitivity Multiplier is open")
        general_settings["Scoped Sensitivity Multiplier"] = readText(image, calibrateDisplay(text_locations.general_sensitivity_scoped_value))
    else:
        print("General - Scoped Sensitivity Multiplier not found")
    time.sleep(delay_times.after_reading_values)

    # Read ADS Sensitivity Multiplier
    if(checkText(image, calibrateDisplay(text_locations.general_sensitivity_ads), text_strings.general_sensitivity_ads)):
        print("ADS Sensitivity Multiplier is open")
        general_settings["ADS Sensitivity Multiplier"] = readText(image, calibrateDisplay(text_locations.general_sensitivity_ads_value))
    else:
        print("General - ADS Sensitivity Multiplier not found")
    time.sleep(delay_times.after_reading_values)

    # Read Invert Mouse
    if(checkText(image, calibrateDisplay(text_locations.general_invert_mouse), text_strings.general_invert_mouse)):
        print("Invert Mouse is open")
        if(compareImages(image, calibrateDisplay(text_locations.general_invert_mouse_on), calibrateDisplay(text_locations.general_invert_mouse_off)) == 1):
            general_settings["Invert Mouse"] = "On"
        elif(compareImages(image, calibrateDisplay(text_locations.general_invert_mouse_on), calibrateDisplay(text_locations.general_invert_mouse_off)) == 2):
            general_settings["Invert Mouse"] = "Off"
        else:
            print("Cannot determine Invert Mouse value")
    else:
        print("General - Invert Mouse not found")
    time.sleep(delay_times.after_reading_values)

    # Read Raw Input Buffer
    if(checkText(image, calibrateDisplay(text_locations.general_input_buffer), text_strings.general_input_buffer)):
        print("Raw Input Buffer is open")
        if(compareImages(image, calibrateDisplay(text_locations.general_input_buffer_on), calibrateDisplay(text_locations.general_input_buffer_off)) == 1):
            general_settings["Raw Input Buffer"] = "On"
        elif(compareImages(image, calibrateDisplay(text_locations.general_input_buffer_on), calibrateDisplay(text_locations.general_input_buffer_off)) == 2):
            general_settings["Raw Input Buffer"] = "Off"
        else:
            print("Cannot determine Raw Input Buffer value")
    else:
        print("General - Raw Input Buffer not found")
    time.sleep(delay_times.after_reading_values)

    # Read Map Rotate
    if(checkText(image, calibrateDisplay(text_locations.general_map_rotate), text_strings.general_map_rotate)):
        print("Map Rotate is open")
        if(compareImages(image, calibrateDisplay(text_locations.general_map_rotate_rotate), calibrateDisplay(text_locations.general_map_rotate_fixed)) == 1):
            general_settings["Map Rotate"] = "Rotate"
        elif(compareImages(image, calibrateDisplay(text_locations.general_map_rotate_rotate), calibrateDisplay(text_locations.general_map_rotate_fixed)) == 2):
            general_settings["Map Rotate"] = "Fixed"

            # Read Fixed Orientation
            if(checkText(image, calibrateDisplay(text_locations.general_map_fixed_orientation), text_strings.general_map_fixed_orientation)):
                print("Fixed Orientation is open")
                if(compareImages(image, calibrateDisplay(text_locations.general_map_fixed_orientation_always_same), calibrateDisplay(text_locations.general_map_fixed_orientation_side_based)) == 1):
                    general_settings["Fixed Orientation"] = "Always the Same"
                elif(compareImages(image, calibrateDisplay(text_locations.general_map_fixed_orientation_always_same), calibrateDisplay(text_locations.general_map_fixed_orientation_side_based)) == 2):
                    general_settings["Fixed Orientation"] = "Based on Side"
                else:
                    print("Cannot determine Fixed Orientation value")
                time.sleep(delay_times.after_reading_values)
        else:
            print("Cannot determine Map Rotate value")
    else:
        print("General - Map Rotate not found")
    time.sleep(delay_times.after_reading_values)

    # Read Player Centered
    if(checkText(image, calibrateDisplay(text_locations.general_player_centered), text_strings.general_player_centered)):
        print("Player Centered is open")
        if(compareImages(image, calibrateDisplay(text_locations.general_player_centered_on), calibrateDisplay(text_locations.general_player_centered_off)) == 1):
            general_settings["Player Centered"] = "On"
        elif(compareImages(image, calibrateDisplay(text_locations.general_player_centered_on), calibrateDisplay(text_locations.general_player_centered_off)) == 2):
            general_settings["Player Centered"] = "Off"
        else:
            print("Cannot determine Player Centered value")
    else:
        print("General - Player Centered not found")
    time.sleep(delay_times.after_reading_values)

    return json.dumps(general_settings)