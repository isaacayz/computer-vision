import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 2)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 2)
    img = cv2.rectangle(img, (100,100), (300, 300), (0,255,60), 4)
    img = cv2.circle(img, (200, 200), 60, (0,0,255), 9)
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, 'Isaac is great', (200, height - 20), font, 2, (0, 128, 128), 5, cv2.LINE_AA)

    cv2.imshow('Frame', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()