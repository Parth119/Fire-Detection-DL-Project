import cv2

import numpy as np

cap = cv2.VideoCapture('.\\video\\test.mp4')
Alarm_Status = False
Email_Status = False
Fire_Reported = 0

while cap.isOpened():

    ret, frame = cap.read()

    if cv2.waitKey(1) == ord('q') or ret == False:
        break

    frame = cv2.bilateralFilter(frame, 9, 75, 75)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_bound = np.array([18, 50, 50])

    u_bound = np.array([39, 255, 255])

    mask = cv2.inRange(hsv, l_bound, u_bound)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    res_con = cv2.bitwise_and(frame, frame, mask=mask)

    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 100, 200)

    _, thr = cv2.threshold(mask, 100, 255, 0)

    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(res_con, contours, -1, (255, 0, 0), 3)

    # cv2.imshow('Original Frame', frame)

    # cv2.imshow('Mask', mask)

    # cv2.imshow('Res', res)
    #
    # cv2.imshow('Res_con', res_con)
    #
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if (area > 1500):
            cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 2)
            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Fire:", (x + w, y + h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # output = cv2.bitwise_and(frame, hsv, mask=mask)
    no_red = cv2.countNonZero(mask)

    if int(no_red) > 1500:
        Fire_Reported = Fire_Reported + 1

    cv2.imshow("Video", frame)
    cv2.imshow("HSV", canny)

cap.release()

cv2.destroyAllWindows()
