
import cv2
import time
import os
   
  
# SET THE COUNTDOWN TIMER
# for simplicity we set it to 3
# We can also take this as input
TIMER = int(2)
   
# Open the camera
cap = cv2.VideoCapture(0)
   
  
while True:
      
    # Read and display each frame
    ret, img = cap.read()
   
  
    # check for the key pressed
    k = cv2.waitKey(125)
  
    # set the key for the countdown
    # to begin. Here we set q
    # if key pressed is q

    while(True):
        if 1 == 1:
            prev = time.time()
  
            while TIMER >= 0:
                ret, img = cap.read()
  
            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
                
            # current time
                cur = time.time()
  
            # Update and keep track of Countdown
            # if time elapsed is one second 
            # then decrease the counter
                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1
  
            else:
                ret, img = cap.read()
  
            # Display the clicked frame for 2 
            # sec.You can increase time in 
            # waitKey also
               
  
            # time for which image displayed
             
  
            # Save the frame
                cv2.imwrite('camera.jpg', img)
                os.system("/usr/local/bin/python3 yolo.py -i camera.jpg")  
  
            # HERE we can reset the Countdown timer
            # if we want more Capture without closing
            # the camera
            
   
  
  
  
# close the camera
cap.release()
   
# close all the opened windows
cv2.destroyAllWindows()
