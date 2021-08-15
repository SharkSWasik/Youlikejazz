import cv2
import numpy as np
import csv



def to_csv(image, dst):
    rects, trash = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    coordinates = []
    for c in rects:
        x, y, w, h = cv2.boundingRect(c)
        if h > 13 and w > 13:
            coordinates.append((x + w // 2,y + h // 2))

    # open the file in the write mode
    f = open(dst+ '.csv', 'w')
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    for row in coordinates:
        writer.writerow([row[1], row[0]])

    # close the file
    f.close()

def postprocessing(preprocess, gray_image):
    preprocess = scipy.ndimage.gaussian_filter(preprocess, sigma=3.0)
    return preprocess

def detect(img):
    dst = cv2.cornerHarris(np.array(img).astype(np.uint8), 32, 5, 0.04)
    dst = cv2.dilate(dst,None)
    img_thresh = cv2.threshold(dst, 0.32*dst.max(), 255, 0)[1]
    img_thresh = np.uint8(img_thresh)
    return img_thresh
