import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
################################
wCam, hCam = 640, 480
################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    # find hand, return hands and img
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)
    # print(lmList) # return self.lmList, bbox
    # self.lmList = (id, cx, cy) : id la vi tri diem theo doi tren ban tay ( 0 - 20)
    # bbox = xmin, ymin, xmax, ymax

    # print(len(lmList))
    # [[0, 169, 430], [1, 230, 416], [2, 279, 378], [3, 307, 338], [4, 321, 301], [5, 256, 307], [6, 285, 260], [7, 304, 230], [8, 321, 202], [9, 228, 293], [10, 254, 239], [11, 273, 202], [12, 290, 169], [13, 198, 290], [14, 219, 236], [15, 237, 201], [16, 254, 169], [17, 165, 296], [18, 178, 252], [19, 191, 223], [20, 205, 195]]
    # print(bbox)
    # (165, 169, 321, 430)

    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        for (id, cx, cy) in lmList:
            if (id % 4) == 0:
        # x1, y1 = lmList[4][1], lmList[4][2]
        # x2, y2 = lmList[8][1], lmList[8][2]
        # cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                cv2.circle(img, (cx, cy), 15, (10*id, 0, 255-10*id), cv2.FILLED)

            # cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            # cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        # length = math.hypot(x2 - x1, y2 - y1)
        # print(length)



        # if length < 50:
        #     cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    # cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    # cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    # cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
    #             1, (255, 0, 0), 3)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    key = cv2.waitKey(1)
    if key == ord("q"):  # press q to exit
        break
