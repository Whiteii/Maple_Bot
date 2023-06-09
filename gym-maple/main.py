import cv2 as cv
import os
from time import time
from windowCapture import window_capture
import numpy as np





import gym 
import gym_maple







# This is an instance of the window_capture class
wincap = window_capture('Maplestory')



from template_matching import ImageMatching


import glob
template_images = [img for img in glob.glob(r'C:\Users\liang\OneDrive\Desktop\Maple_Bot\Asset\Hero_Skills\*.png')] 

template_images = template_images + [img for img in glob.glob(r'C:\Users\liang\OneDrive\Desktop\Maple_Bot\Asset\Temple Of Time\*.png')] 


#Creating an instance of gym Environment 
env = gym.make('gym_maple/MapleEnv-v0')
print(env.observation_space) 

env.reset()







loop_time = time()
while True:
    frame = wincap.screenshot()
    main_image = cv.imwrite('main_image.png',frame) # create it
    #print(main_image)
    image_match = ImageMatching('main_image.png', 0.75)
    
    #these dictionary value will be representing as info capture by CV
    dictionary = image_match.template_matching(template_images)
 
    step = env.step(dictionary)
    
    # Calculate FPS
    ##print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()



    # Break the loop when 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
