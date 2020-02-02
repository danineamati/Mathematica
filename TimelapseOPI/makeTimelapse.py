# OPI Timelapse Attempt
# Daniel Neamati
# 28 January 2020

import cv2
import os

image_folder = 'rawPhotos'
video_name = 'OPIvideo.avi'


print("Getting images")
images = [img for img in os.listdir(image_folder) if img.endswith(".JPG")]

print("Preparing frame and video")
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fps = 60.0
video = cv2.VideoWriter(video_name, 0, fps, (width,height))

print("Writing Video...")
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

print("Vidoe Writing Complete. Exitting.")
cv2.destroyAllWindows()
video.release()

print("Complete!!")
print("Video is called {}".format(video_name))