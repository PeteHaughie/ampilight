#!/usr/bin/env python

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    img = cv2.resize(frame, None, fx=0.107, fy=0.107)
    cv2.imwrite("output.png", img)
    time.sleep(1/20)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
