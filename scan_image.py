#!/usr/bin/env python
import cv2
import numpy as np
import time

f = open('values.json', 'w')
rgb = []
left = []
right = []
top = []

def Reverse(lst):
  lst.reverse()
  return lst

def pixelValues():
  img = cv2.imread('gradient.png')
  height, width, channels = img.shape
  for y in range(height):
    if y == 0:
      for x in range(width):
        rgb = []
        rgb.append(img[y, x][0])
        rgb.append(img[y, x][1])
        rgb.append(img[y, x][2])
        top.append(rgb)
    else:
      for x in range(width):
        if x == 0:
          rgb = []
          rgb.append(img[y, x][0])
          rgb.append(img[y, x][1])
          rgb.append(img[y, x][2])
          left.append(rgb)
        if x == width - 1:
          rgb = []
          rgb.append(img[y, x][0])
          rgb.append(img[y, x][1])
          rgb.append(img[y, x][2])
          right.append(rgb)
  orderedList = Reverse(left) + top + right
  f.write(str(orderedList))

pixelValues()
# print("array lengths")
# print(len(top), len(left), len(right))
# print("first array position, r, g, b ")
# print("top")
# print(top[0][0], top[0][1], top[0][2])
# print("left")
# print(left)
# print("left reversed")
# print(Reverse(left))
# print("right")
# print(right[0][0], right[0][1], right[0][2])
f.close()
