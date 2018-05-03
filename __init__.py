import cv2
import numpy as np
from performRecognition import PerfRecognition

# Start capturing the video using laptop webcam
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
# Initialize Centroid
pre_cx = 0;
pre_cy = 0;

i = False

operation = 0
count = 0;
# Creates an empty Canvas
img = np.zeros((480, 640, 3), np.uint8)
img = cv2.flip(img, 1)



a = 0
b= 0

pr = PerfRecognition()
res=''


def nothing():
    pass

# # assign strings for ease of coding
# hh = 'Hue High'
# hl = 'Hue Low'
# sh = 'Saturation High'
# sl = 'Saturation Low'
# vh = 'Value High'
# vl = 'Value Low'
# wnd = 'Colorbars'

# # Begin Creating trackbars for each
# cv2.createTrackbar(hl, wnd, 110, 179, nothing)
# cv2.createTrackbar(hh, wnd, 130, 179, nothing)
# cv2.createTrackbar(sl, wnd, 50, 255, nothing)
# cv2.createTrackbar(sh, wnd, 255, 255, nothing)
# cv2.createTrackbar(vl, wnd, 50, 255, nothing)
# cv2.createTrackbar(vh, wnd, 255, 255, nothing)

is_predict = False
while (1):
    # Take each frame
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # read trackbar positions for each trackbar
    # hul = cv2.getTrackbarPos(hl, wnd)
    # huh = cv2.getTrackbarPos(hh, wnd)
    # sal = cv2.getTrackbarPos(sl, wnd)
    # sah = cv2.getTrackbarPos(sh, wnd)
    # val = cv2.getTrackbarPos(vl, wnd)
    # vah = cv2.getTrackbarPos(vh, wnd)
    
    # # make array for final values
    # HSVLOW = np.array([hul, sal, val])
    # HSVHIGH = np.array([huh, sah, vah])

    # Array of HSV Bounds
    lower_blue = np.array([111, 65, 104])
    upper_blue = np.array([179, 255, 255])

    lower_green = np.array([40,30,50])
    upper_green = np.array([77,255,255])

    # Mask the hsv to the image
    mask = cv2.inRange(hsv, lower_green, upper_green)
    #cv2.imshow("MASK", mask)

    # Reduce noise using Median Blur Filter
    median = cv2.medianBlur(mask, 5)
    #cv2.imshow('FRAME', median)

    # Detect the contours and sorts them according to their area
    im2, contours, hie = cv2.findContours(median, 1, 2)
    cnt_sort = sorted(contours, key=cv2.contourArea, reverse=True)

    # Find moments of the largest contour
    if cnt_sort:
        M = cv2.moments(cnt_sort[0])
        if M['m00'] != 0:
             # Centroid of the object
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            #print cv2.contourArea(cnt_sort[0])

            if cv2.contourArea(cnt_sort[0]) > 1400.0:
                if i:
                    # Draw line from previous centroid to the new centroid of the object
                    cv2.line(img, (pre_cx, pre_cy), (cx, cy), (255, 255, 255), 4)

                else:
                    i = True
                    is_predict = True
                pre_cy = cy
                pre_cx = cx
            else:
                img2 = np.zeros((200, 640, 3), np.uint8)

                if (cx > 5 and cx < 40 and cy > 5 and cy < 40 and is_predict):
                    print 'this1'
                    cv2.imwrite('photo.jpg', img)
                    if (count == 0):
                        operation = 0
                        a = pr.predict()
                        img2 = np.zeros((200, 640, 3), np.uint8)
                        res = str(a)
                        cv2.putText(img2, res, (250, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                        count = 1
                    else:
                        b = pr.predict()
                        a = pr.operation(operation, a, b)
                        if(operation == 0):
                            res = res +'+'+ str(b)
                        elif operation == 1:
                            res = res +'-'+str(b)
                        elif operation == 2:
                            res = res +'*'+str(b)
                        operation = 0
                        print res
                        
                        cv2.putText(img2, res+'='+str(a), (250, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                        print 'your answer is ' + str(a)
                    is_predict = False
                    cv2.imshow("MATHS", img2)
                    img = np.zeros((480, 640, 3), np.uint8)
                    img = cv2.flip(img, 1)
                elif (cx > 600 and cx < 635 and cy > 5 and cy < 40 and is_predict):
                    print 'this2'
                    cv2.imwrite('photo.jpg', img)
                    if (count == 0):
                        operation = 1
                        a = pr.predict()
                        img2 = np.zeros((200, 640, 3), np.uint8)
                        res = str(a)
                        cv2.putText(img2, res, (250, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                        count = 1
                    else:
                        b = pr.predict()
                        a = pr.operation(operation, a, b)
                        if(operation == 0):
                            res = res +'+'+ str(b)
                        elif operation == 1:
                            res = res +'-'+str(b)
                        elif operation == 2:
                            res = res +'*'+str(b)
                        operation = 1
                        print res
                        
                        cv2.putText(img2, res+'='+str(a), (250, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                        print 'your answer is ' + str(a)
                    is_predict = False
                    cv2.imshow("MATHS", img2)
                    img = np.zeros((480, 640, 3), np.uint8)
                    img = cv2.flip(img, 1)

                elif (cx > 5 and cx < 40 and cy > 440 and cy < 475 and is_predict):
                    print 'this3'
                    cv2.imwrite('photo.jpg', img)
                    if (count == 0):
                        operation = 2
                        a = pr.predict()
                        img2 = np.zeros((200, 640, 3), np.uint8)
                        res = str(a)
                        cv2.putText(img2, res, (250, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                        count = 1
                    else:
                        b = pr.predict()
                        a = pr.operation(operation, a, b)
                        if(operation == 0):
                            res = res +'+'+ str(b)
                        elif operation == 1:
                            res = res +'-'+str(b)
                        elif operation == 2:
                            res = res +'*'+str(b)
                        operation = 2
                        print res
                        cv2.putText(img2, res+'='+str(a), (250, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                        print 'your answer is ' + str(pr.operation(operation, a, b))
                    is_predict = False
                    cv2.imshow("MATHS", img2)
                    img = np.zeros((480, 640, 3), np.uint8)
                    img = cv2.flip(img, 1)
                elif (cx > 600 and cx < 635 and cy > 440 and cy < 475 and is_predict):
                    print 'this4'
                    cv2.imwrite('photo.jpg', img)
                    if count !=0 :
                        b = pr.predict()
                        if(operation == 0):
                            res = res +'+'+ str(b)
                        elif operation == 1:
                            res = res +'-'+str(b)
                        elif operation == 2:
                            res = res +'*'+str(b)
                        
                        a = pr.operation(operation, a, b)
                        cv2.putText(img2, res+'='+str(a), (250, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
                        print 'your answer is ' + str(a)
                        count = 0
                        operation = 0
                        a = 0
                        b = 0 
                        res = ''
                    is_predict = False
                    cv2.imshow("MATHS", img2)
                    img = np.zeros((480, 640, 3), np.uint8)
                    img = cv2.flip(img, 1)
                #print str(cx)+","+str(cy)
                # cv2.circle(img, (cx, cy), 5, [255,0,0], -1)
                # flip = cv2.flip(img, 1)
                # cv2.imshow('image', flip)
                i = False
        #cv2.imwrite('photo.jpg', flip)
    frame = cv2.addWeighted(img,1.0, frame,0.5, 0)
    cv2.rectangle(frame,(5,5),(40,40),(0,255,255),3)
    cv2.putText(frame, '+', (10, 30),cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
    cv2.rectangle(frame,(600,5),(635,40),(0,255,255),3)
    cv2.putText(frame, '-', (608, 30),cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
    cv2.rectangle(frame,(5,440),(40,475),(0,255,255),3)
    cv2.putText(frame, '*', (15, 470),cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
    cv2.rectangle(frame,(600,440),(635,475),(0,255,255),3)
    cv2.putText(frame, '=', (605, 465),cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
    cv2.imshow('image', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        cv2.imwrite('photo.jpg', img)
        break
        
cv2.destroyAllWindows()
