import time
import nltk
import pygetwindow as gw

def openApplication(name):
    try:
        window_list = gw.getWindowsWithTitle(name)
        index = 0
        dist = 100000 # arbitrary large number
        print("Window list: ", window_list)
        for ind, window in enumerate(window_list):
            print(ind, window.title)
            if(nltk.edit_distance(window.title, name) < dist):
                dist = nltk.edit_distance(window.title, name)
                index = ind
        window = window_list[index]

        if window.isMinimized:
            window.maximize()
        window.activate()

    # except IndexError:
    #     print("Application not found")
    except Exception as e:
        print("Exception occurred, details below:")
        print(e)