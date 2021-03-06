#!/usr/bin/env python
import cv2
import numpy as np
import time

def pixelValues():
  img = cv2.imread('gradient.png')
  height, width, channels = img.shape
  for y in range(height):
    for x in range(width):
      print(img[y, x])

while True:
  pixelValues()
  time.sleep(1/20)
