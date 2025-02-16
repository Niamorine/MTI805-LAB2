import numpy as np
import cv2

def drawMatches(img1, kp1, img2, kp2, matches):
    """
    img1,img2 - Grayscale images
    kp1,kp2 - Detected list of keypoints through any of the OpenCV keypoint 
              detection algorithms
    matches - A list of matches of corresponding keypoints through any
              OpenCV keypoint matching algorithm
    """

    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]
    
    buf_h = 100

    out = np.full((max([rows1,rows2]),cols1 + buf_h + cols2, 3), 255, dtype='uint8')

    out[:rows1,:cols1,:] = img1

    out[:rows2,cols1 + buf_h:cols1 + buf_h + cols2,:] = img2

    for mat in matches:

        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt

        rad = 20
        cv2.circle(out, (int(x1),int(y1)), 4, (0, 0, 255), rad)   
        cv2.circle(out, (int(x2)+cols1+buf_h,int(y2)), 4, (0, 0, 255), rad)

        cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1+buf_h,int(y2)), (255, 0, 0), 3)

    return out


img1 = cv2.imread('assets/inazuma1.png')
img2 = cv2.imread('assets/inazuma2.png')

sift = cv2.SIFT.create()

(kp1,des1) = sift.detectAndCompute(img1, None)
(kp2,des2) = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher.create()

matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda val: val.distance)

out = drawMatches(img1, kp1, img2, kp2, matches[:10])

cv2.imwrite('matches/matches.jpg', out)