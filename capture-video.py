# PROPERLY CAPTURES PHONE

"""

Improvements from provided OpenCV Object Tracking code (https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html):

    - Adjusted HSV range to be more specific from the original code
    - Added contour detection and bounding boxes for better visualization
    - Displays original frame with highlighted blue areas
    - Enhanced user experience with improved visual feedback
    - Loop exits on pressing 'ESC' key

"""

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Define range of blue color in HSV
    lowerBlue = np.array([110, 50, 50])
    upperBlue = np.array([120, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lowerBlue, upperBlue)

    # Find contours in the mask
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw a detection box around blue colors
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the original frame with detection box
    cv.imshow('frame', frame)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()