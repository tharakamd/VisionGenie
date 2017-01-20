
import cv2
import numpy as np

class DrawMatchFile:
    def drawMatches(self,img1, kp1, img2, kp2, matches):
        # Create a new output image that concatenates the two images together
        # (a.k.a) a montage
        rows1 = img1.shape[0]
        cols1 = img1.shape[1]
        rows2 = img2.shape[0]
        cols2 = img2.shape[1]

        out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')

        # Place the first image to the left
        out[:rows1,:cols1] = np.dstack([img1, img1, img1])

        # Place the next image to the right of it
        out[:rows2,cols1:] = np.dstack([img2, img2, img2])

        distance_diff_list =[];
        distance_list =[];

        # For each pair of points we have between both images
        # draw circles, then connect a line between them
        for mat in matches:

            # Get the matching keypoints for each of the images
            img1_idx = mat.queryIdx
            img2_idx = mat.trainIdx

            # x - columns
            # y - rows
            (x1,y1) = kp1[img1_idx].pt
            (x2,y2) = kp2[img2_idx].pt

            print (x2-x1)
            distance_list.append(y1)
            distance_diff_list.append(y2-y1)

            # # print (x2,y2)
            # print "----"

            # Draw a small circle at both co-ordinates
            # radius 4
            # colour blue
            # thickness = 1
            cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0) , 1)
            cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)

            # Draw a line in between the two points
            # thickness = 1
            # colour blue
            cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)


        # print distance_list
        # Show the image
        # cv2.imshow('Matched Features', out)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     cv2.destroyWindow('Matched Features')

        avg_diff = np.mean(distance_diff_list)         #get the average of the moved distances
        avg_dist =  np.mean(distance_list)              #get the average of original distance

        output_array =[avg_diff,avg_dist]
        


        # Also return the image if you'd like a copy
        return output_array

