# PROPERLY CAPTURES DOMINANT COLOR IN CENTRAL RECTANGLE

"""

Improvements from provided OpenCV Object Tracking code (https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html):

    - Added a 'find_dominant_color' function for K-means based dominant color extraction
    - Created windows for 'Video Feed' and 'Dominant Color' using 'cv.namedWindow'
    - Converted BGR frame to RGB for processing
    - Defined and extracted a central rectangle within the frame
    - Calculated the dominant color using 'find_dominant_color' on the central rectangle
    - Drew a green rectangle around the central region on the original frame
    - Displayed the color swatch representing the dominant color in the 'Dominant Color' window
    - Loop exits on pressing 'ESC' key
    - Released the video capture object and closed all windows for cleanup

"""

import cv2 as cv
import numpy as np

def find_dominant_color(image):

    # Convert image to 1D array
    pixels = image.reshape(-1, 3)

    # Convert to 32-bit float
    pixels = np.float32(pixels)

    # Perform K-means clustering
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv.kmeans(pixels, 1, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    # Convert center to 8-bit integer
    dominant_color = np.uint8(centers[0])

    return dominant_color

cap = cv.VideoCapture(0)

# Create a window for the video feed
cv.namedWindow('Video Feed')

# Create a window for the dominant color swatch
cv.namedWindow('Dominant Color')

while True:

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to RGB
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Extract the central rectangle (adjust dimensions as needed)
    x, y, w, h = frame.shape[1] // 4, frame.shape[0] // 4, frame.shape[1] // 2, frame.shape[0] // 2
    central_rect = rgb_frame[y:y+h, x:x+w]

    # Find the dominant color in the central rectangle using K-means
    dominant_color = find_dominant_color(central_rect)

    # Draw the outline of the central rectangle on the frame
    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frames
    cv.imshow('Video Feed', frame)

    # Display the dominant color swatch
    color_swatch = np.zeros((100, 100, 3), dtype=np.uint8)
    color_swatch[:, :] = dominant_color
    cv.imshow('Dominant Color', color_swatch)

    # Break the loop if 'ESC' key is pressed
    if cv.waitKey(1) == 27:
        break

# Release the video capture object and close all windows
cap.release()
cv.destroyAllWindows()