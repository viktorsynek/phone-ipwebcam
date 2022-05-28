#  Accessing Phone's Camera in Python | Created by Viktor Synek
Accessing Phone's camera with IP Webcam + modules cv2

The user starts a server within the app IP Webcam and sets the IP in the code to the given IP address.

The program detects motions and draw a rectangle at them.

If there is motion detected - Creates and saves images to the folder.

The image is gonna get a gray filter once the time is over 10 PM.

The DATA.txt holds a number in it - how many images were created. 
It resets to 0 everytime you press q!

(The program can be stopped by pressing the q button!)


NOTE! The program is a bit laggy, which is understandable because it's creating tons of images once there is motion
detected.. And also it's using IP Webcam app which is free to use, and can't handle that many informations!
The program can be buggy, it's actually looking for pixel changes, if there is, then it detects the motion..
So at night the program will see no pixel changes because it's so dark!


Source code with comments. Used 4 modules [cv2, datetime, numpy, pyautogui] 

[Viktor Synek Twitter](https://www.twitter.com/vAnonyms)
