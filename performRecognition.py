# Import the modules
import cv2
from keras.models import load_model
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np

class PerfRecognition:
    def operation(self, op, a, b):
        if op == 0:
            return a+b
        elif op == 1:
            return a - b
        elif op == 2:
            return a * b

    def predict(self):
        # Load the classifier
        clf = joblib.load("digits_cls.pkl")
        model = load_model('my_model.h5')

        # Read the input image 
        im = cv2.imread('photo.jpg')

        # Convert to grayscale and apply Gaussian filtering
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

        # ##applying erosion 
        # kernel = np.ones((3,3), np.uint8)
        # erosion = cv2.erode(im_gray,kernel, iterations = 1)
        # cv2.imshow("erode",erosion)



        # Threshold the image
        ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY)
        #cv2.imshow("image_threshold", im_th)

        # Find contours in the image
        im2, ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ctrs_sort = sorted(ctrs, key=cv2.contourArea, reverse=True)
        if ctrs_sort:
            # Get rectangles contains each contour
            rects = [cv2.boundingRect(ctrs_sort[0])]


            # For each rectangular region, calculate HOG features and predict
            # the digit using Linear SVM.

            for rect in rects:
                # Draw the rectangles
                cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
                
                # Make the rectangular region around the digit
                leng = int(rect[3] * 1.6)
                pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
                pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
                print pt1
                print pt2
                print leng
                roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
                #cv2.imshow("frame_2", roi)
                # Resize the image
                roi = cv2.resize(roi, (28,28), interpolation=cv2.INTER_AREA)
                roi = cv2.dilate(roi, (3, 3), iterations = 2)
                
                # Calculate the HOG features
                r = np.array(roi).flatten()
                print r
                t = r.reshape((1,784))
                print t.shape
                nbr = model.predict(t)
                return int(nbr.argmax())
