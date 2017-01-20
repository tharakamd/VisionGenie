import cv2
import numpy

from AbstractImageProcessor import AbstractImageProcessor
from DrawMatchFile import DrawMatchFile
from Sensors.Gyroscope import Gyroscope

class BinacularVisionImageProcessor(AbstractImageProcessor):
    dmf = None
    orb = None
    bf = None

    image1 = None # frame one
    image2 = None # frame two

    frame_count = None; # the frame number

    def __init__(self):
        # print self.getMatchedDetails()
        self.dmf = DrawMatchFile()
        self.orb = cv2.ORB_create()
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        self.frame_count = 0

    def update(self, frame):
        if(self.image1 is None and self.image2 is None):
            self.image1 = numpy.empty_like(frame)
            self.image2 = numpy.empty_like(frame)
            numpy.copyto(self.image1,frame)
            numpy.copyto(self.image2,frame)
            self.frame_count = 0
        else:
            if(self.frame_count >=10): # frame replace should take place
                numpy.copyto(self.image1, self.image2)
                numpy.copyto(self.image2,frame)
                self.frame_count = 0
                self.calculateDistance(self.getMatchedDetails(self.image1,self.image2))
            else:
                self.frame_count += 1

    def getMatchedDetails(self,img1,img2):


        # image1 = preprocess.image1;     #previous frame
        # image2 = preprocess.image2;     #current frame

        orb = self.orb
        dmf = self.dmf

        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)

        # create BFMatcher object
        bf = self.bf

        # Match descriptors.
        matches = bf.match(des1,des2)


        # Sort them in the order of their distance.l
        matches = sorted(matches, key = lambda x:x.distance)

        # get distance list frommatching points
        dist_list = dmf.drawMatches(img1,kp1,img2,kp2,matches[:10])


        return dist_list

    def calculateDistance(self, output_array):

        gyroscope = Gyroscope;
        # velocity = gyroscope.velocity;

        time_period = 1         #this can be vary with the frame difference

        # print output_array
        image_valocity = output_array[0]/time_period
        actual_velocity = 0.5       # this is to be read by gyroscope
        image_distance = output_array[1]

        actual_distance = abs((actual_velocity/image_valocity)*image_distance)

        print actual_distance

        return ;



