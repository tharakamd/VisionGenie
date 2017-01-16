import cv2

from AbstractImageProcessor import AbstractImageProcessor
from DrawMatchFile import DrawMatchFile
from Sensors.Gyroscope import Gyroscope

class BinacularVisionImageProcessor(AbstractImageProcessor):

    def __init__(self):
        # print self.getMatchedDetails()
        self.calculateDistance(self.getMatchedDetails())

    def update(self, frame):


    def getMatchedDetails(self):
        dmf = DrawMatchFile()

        # image1 = preprocess.image1;     #previous frame
        # image2 = preprocess.image2;     #current frame

        image1 = cv2.imread('tennis.png')       #temporary image
        image2 = cv2.imread('tenni.png')        #temporary image
        img1 =  cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        img2 =   cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


        orb = cv2.ORB()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)

        # create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors.
        matches = bf.match(des1,des2)


        # Sort them in the order of their distance.l
        matches = sorted(matches, key = lambda x:x.distance)

        # get distance list frommatching points
        dist_list = dmf.drawMatches(img1,kp1,img2,kp2,matches[:10])

        # cv2.imshow('Matched Features', img3)
        # cv2.waitKey(0)
        # cv2.destroyWindow('Matched Features')
        return dist_list

    def calculateDistance(self, output_array):

        gyroscope = Gyroscope;
        # velocity = gyroscope.velocity;

        time_period = 1         #this can be vary with the frame difference

        print output_array
        image_valocity = output_array[0]/time_period
        actual_velocity = 0.5       # this is to be read by gyroscope
        image_distance = output_array[1]

        actual_distance = (actual_velocity/image_valocity)*image_distance

        print actual_distance

        return ;

x= BinacularVisionImageProcessor();

