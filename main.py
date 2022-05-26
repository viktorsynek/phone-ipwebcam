############################################   -== INFORMATION ==-   ############################################

#### ACCESS YOUR PHONE'S WEBCAM VIA APP "IP Webcam" + THIS CODE
#### THE PROGRAM WAS CREATED AND PUBLISHED BY:
#### https://github.com/viktorsynek
#### https://twitter.com/vAnonyms

#############################################   -== PROGRAM ==-   ###############################################

# IMPORT LIBRARIES
import cv2
import datetime
import numpy as np
import pyautogui


video = cv2.VideoCapture(0)
# DOWNLOAD "IP Webcam" APP TO YOUR PHONE, START THE SERVER AND ASSIGN YOUR IP TO THE ADDRESS VARIABLE 
address = "http://192.168.0.191:8080/video" # IP HERE
video.open(address)

while True:
    ret, frame1 = video.read()
    ret, frame2 = video.read()

    # SHOW CURRENT TIME
    font = cv2.FONT_HERSHEY_SIMPLEX
    now = str(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
    frame = cv2.putText(frame1, now, (10, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # CREATE MOTION
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   

    # GET CURRENT TIME
    hm = float(datetime.datetime.now().strftime("%H.%M"))

    # CREATING THE RECTANGLES IF THERE IS SOME PIXEL CHANGE
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 4800:
            continue
        
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # CREATE A SCREENSHOT ONCE THERE WAS A MOTION DETECTED
        image = pyautogui.screenshot()
        # IF THE TIME IS MORE THAN 10 PM THE IMAGES WILL BE SAVED WITH A GRAY FILTER
        if hm > 22.00:
            image = cv2.cvtColor(np.array(image),
                cv2.COLOR_RGB2GRAY)
        # OTHERWISE WITH A NORMAL FILTER
        else:
            image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR)
        
        # OPEN THE DATA.TXT FILE
        fileDataRead = open("DATA.txt", "r")
        # READ THE DATA.TXT FILE
        fileDataName = fileDataRead.read()

        # SAVE THE IMAGES INTO THE DIRECTORY
        cv2.imwrite(f"image{fileDataName}.png", image)
        # IF AN IMAGE WAS CREATED ADD +1 TO THIS VARIABLE
        newData = int(fileDataName) + 1

        # OPEN THE DATA.TXT FILE
        fileDataWrite = open("DATA.txt", "w")
        # WRITE THE DATA.TXT FILE HOW MANY IMAGES WAS CREATED
        fileDataWrite.write(str(newData))
        fileDataWrite.close()
        # SOME TEXT WHENEVER MOTION WAS CREATED
        cv2.putText(frame1, "Status: {}".format('Motion detected'), (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 3)
            
            
    # THE TITLE OF THE WINDOW
    cv2.imshow('Camera', frame1)
    frame1 = frame2
    ret, frame2 = video.read()
    # IF YOU PRESS "Q"
    if cv2.waitKey(1) == ord('q'):
        # REWRITE, RESET DATA.TXT TO 0 
        fileDataWrite = open("DATA.txt", "w")
        fileDataWrite.write(str(0))
        fileDataWrite.close()
        # STOP THE PROGRAM
        cv2.destroyAllWindows
        break

