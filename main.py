import cv2 as cv
import os
from time import time
from windowCapture import window_capture

# This is an instance of the window_capture class
wincap = window_capture('Maplestory')

loop_time = time()

while True:
    # Capture the frame
    frame = wincap.screenshot()

    # Save the frame as a PNG image
    cv.imwrite('main_image.png', frame)

    # Load the main image and template image
    main_image = cv.imread('main_image.png')
    template_images = cv.imread('pot.PNG')

    # Convert both images to grayscale
    main_gray = cv.cvtColor(main_image, cv.COLOR_BGR2GRAY)
    template_gray = cv.cvtColor(template_images, cv.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv.matchTemplate(main_gray, template_gray, cv.TM_CCOEFF_NORMED)

    # Get the location of the best match
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + template_images.shape[1], top_left[1] + template_images.shape[0])

    # Draw a rectangle around the matched region
    cv.rectangle(main_image, top_left, bottom_right, (0, 255, 0), 2)

    # Display the resulting frame
    cv.imshow('Computer Vision', frame)

    # Remove the main_image.png file
    os.remove('main_image.png')

    # Calculate the frame rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break










