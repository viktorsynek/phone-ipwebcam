#  Accessing Phone's Camera with Python | Created by Viktor Synek
Accessing Phone's camera with IP Webcam (on Android) + cv2 module

The user starts a server within the IP Webcam app and sets the IP in the code to their given IP address.

The program detects motions and draws rectangles around them.

If there is motion detected - Creates and saves images to the folder.

The image is gonna get a gray filter once the time is over 10 PM.

The DATA.txt holds a number in it - how many images were created. 
It resets to 0 everytime you stop the program!

(The program can be stopped by pressing the q button!)


NOTE! The program is a bit laggy, which is understandable because it's creating tons of images once there is motion
detected.. And also it's using IP Webcam which is a totally free to use app, so it can not handle this much requests!

It was a great learning project, because I learnt how the cv2 python module is able to handle motion detections.
