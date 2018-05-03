import cv2
import numpy as np


def draw_hand_rect(frame):  
    rows,cols,_ = frame.shape

    hand_row_nw = np.array([6*rows/20,6*rows/20,6*rows/20,10*rows/20,10*rows/20,10*rows/20,14*rows/20,14*rows/20,14*rows/20])

    hand_col_nw = np.array([9*cols/20,10*cols/20,11*cols/20,9*cols/20,10*cols/20,11*cols/20,9*cols/20,10*cols/20,11*cols/20])

    hand_row_se = hand_row_nw + 10
    hand_col_se = hand_col_nw + 10

    size = hand_row_nw.size
    for i in xrange(size):
        cv2.rectangle(frame,(hand_col_nw[i],hand_row_nw[i]),(hand_col_se[i],hand_row_se[i]),(0,255,0),1)
        black = np.zeros(frame.shape, dtype=frame.dtype)
        frame_final = np.vstack([black, frame])
        return frame_final

camera = cv2.VideoCapture(0)

while(True):
    ret, frame = camera.read()

    cv2.imshow("frame-1", draw_hand_rect(frame))
    if cv2.waitKey(1) == ord('q') & 0xFF:
            break

cv2.destroyAllWindows() 
