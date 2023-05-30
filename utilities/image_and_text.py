import cv2 as cv
import pytesseract

def calibrateDisplay(new_size, coordinates):
    if(len(coordinates) == 2):
        return (coordinates[0] * new_size[0] / 1080, coordinates[1] * new_size[1] / 1920)
    elif(len(coordinates) == 4):
        return (coordinates[0] * new_size[0] / 1080, coordinates[1] * new_size[0] / 1080, coordinates[2] * new_size[1] / 1920, coordinates[3] * new_size[1] / 1920)
        

def checkText(image, box, text):
    img = image[box[0]:box[1], box[2]:box[3]]
    ocr = pytesseract.image_to_string(img).strip()
    print(ocr)
    if ocr.lower() == text.lower():
        return True
    else:
        return False
    
def readText(image, box):
    img = image[box[0]:box[1], box[2]:box[3]]
    ocr = pytesseract.image_to_string(img)
    return ocr

def compareImages(image, box1, box2):
    image1 = image[box1[0]:box1[1], box1[2]:box1[3]]
    image2 = image[box2[0]:box2[1], box2[2]:box2[3]]

    # Get sum of all pixel values in the image
    sum1 = cv.sumElems(image1)
    sum2 = cv.sumElems(image2)

    # Get average of all pixel values in the image
    avg1 = sum1[0] / (image1.shape[0] * image1.shape[1])
    avg2 = sum2[0] / (image2.shape[0] * image2.shape[1])

    if(avg1 > avg2):
        return 1
    elif(avg1 < avg2):
        return 2
    else:
        return 0