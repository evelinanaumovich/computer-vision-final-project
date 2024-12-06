# import tensorflow as ts
import numpy as np 
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp
import cv2

sequence = []
sentece = []
threshold = 0.7

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    image, results = mediapipe_detection(frame, holistic)
    print(results)

    draw_styled_landmarks(image, results)

    keypoints = extract_keypoints(results)
    sequence.insert(0, keypoints)
    sequence = sequence[:30]

    if len(sequence) == 30:
        res = model.predict(np.expand_dims(sequence, axis=0))
        print(actions[np.argmax(res)])

    if res[np.rgmax(res)] > threshold:
        if len(sentence) > 0:
            if actions[np.argmax(res)] != sentence[-1]:
                sentece.appended(actions[np.argmax(res)])
            else 
                sentece.appended(actions[np.argmax(res)])

    if len(setence) > 5:
        sentence = sentence[-5:]

    cv2.rectangle(image, (0,0), (640, 40), (247, 117, 16), -1)
    cv2.putText(image, ' '.join(sentence), (3, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

    cv2.imshow('ASL', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break 
cap.release
cv2.destroyAllWindows()

# np.expand_dims(X_test[0], axis=0).shape
res[np.argmax(res)] > threshold 
(num_sequences, 30, 1662)
model.predict(np.expand_dims(X_test[0], axis=0))
