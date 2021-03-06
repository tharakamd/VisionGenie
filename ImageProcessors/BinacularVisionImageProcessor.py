import cv2
import numpy
import logging

from AbstractImageProcessor import AbstractImageProcessor
from DrawMatchFile import DrawMatchFile
from Sensors.Gyroscope import Gyroscope
from Sound.SoundGenerator import SoundGenerator
from Sensors.DistanceHelper import DistanceHelper

class BinacularVisionImageProcessor(AbstractImageProcessor):
    dmf = None
    orb = None
    bf = None

    image1 = None # frame one
    image2 = None # frame two

    frame_count = None; # the frame number

    early_dist =[1]*2;

    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)
        # print self.getMatchedDetails()
        self.dmf = DrawMatchFile()
        self.orb = cv2.ORB_create()
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        self.frame_count = 0
        self.soundGen = SoundGenerator()
        self.distance_helper = DistanceHelper()

    def update(self, frame):
        if(self.image1 is None and self.image2 is None):
            self.image1 = numpy.empty_like(frame)
            self.image2 = numpy.empty_like(frame)
            numpy.copyto(self.image1,frame)
            numpy.copyto(self.image2,frame)
            self.frame_count = 0
        else:
            if(self.frame_count >=2): # frame replace should take place
                numpy.copyto(self.image1, self.image2)
                numpy.copyto(self.image2,frame)
                self.frame_count = 0
                self.calculateDistance(self.getMatchedDetails(self.image1,self.image2))
            else:
                self.frame_count += 1

    def cropImage(self,image):

        height, width = image.shape[:2]
        crop_img = image[0:height, width/5:4*(width/5)]
        return crop_img;

    def getMatchedDetails(self,img1,img2):


        # image1 = preprocess.image1;     #previous frame
        # image2 = preprocess.image2;     #current frame

        orb = self.orb
        dmf = self.dmf

        image1 = self.cropImage(img1)
        image2 = self.cropImage(img2)

        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(image1,None)
        kp2, des2 = orb.detectAndCompute(image2,None)

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
        time_period = 1         #this can be vary with the frame difference
        image_valocity = output_array[0]/time_period
        actual_velocity = 0.5       # this is to be read by gyroscope
        image_distance = output_array[1]
        actual_distance = int(min(abs((actual_velocity/image_valocity)*image_distance),99))+1 # +1 to avoid getting 0

        early_dist_diff = abs(self.early_dist[0] - self.early_dist[1]) #get difference of early distances
        new_dist_diff = actual_distance-self.early_dist[1]      #get difference of latest distances

        if early_dist_diff == 0:
            early_dist_diff = self.early_dist[1];

        if(new_dist_diff> 10*early_dist_diff):
            actual_distance = int((self.early_dist[1]+self.early_dist[0])/2);

        self.early_dist[0]=self.early_dist[1];
        self.early_dist[1]= actual_distance;
        logging.info("Distance : " + str(actual_distance) )
        self.soundGen.updateDistance(actual_distance)



