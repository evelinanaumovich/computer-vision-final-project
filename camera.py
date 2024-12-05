import tensorflow as ts
import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', cv2.resize(frame, (800, 800)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 
