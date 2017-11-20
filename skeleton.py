# import the necessary packages
import numpy as np
import argparse
import cv2

self.video_capture = cv2.VideoCapture()
def _get_video_frame(self):
    # get latest frame from video
    success, frame = self.video_capture.read()
    if success: return frame

    if not self.video_capture.isOpened():
        self.video_capture.open('video/channel_one.mp4')
    else:
        self.video_capture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)

    return self.video_capture.read()[1]


# convert image to OpenGL texture format
tx_image = cv2.flip(frame, 0)
tx_image = Image.fromarray(tx_image)
ix = tx_image.size[0]
iy = tx_image.size[1]
tx_image = tx_image.tobytes('raw', 'BGRX', 0, -1)

# create texture
texture_id = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, tx_image)

glBindTexture(GL_TEXTURE_2D, texture_id)
glBegin(GL_POLYGON)
glTexCoord2fv([0.0, 0.0])
glVertex3fv([1.1, 1.1, -1.1])
glTexCoord2fv([1.0, 0.0])
glVertex3fv([0.0, 1.1, -1.1])
glTexCoord2fv([1.0, 1.0])
glVertex3fv([0.0, 1.1, 0.0])
glTexCoord2fv([0.0, 1.0])
glVertex3fv([1.1, 1.1, 0.0])
glEnd()