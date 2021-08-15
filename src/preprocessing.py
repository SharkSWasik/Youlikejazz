from skimage import color
import cv2
import numpy as np
from skimage.filters import threshold_sauvola

def to_gray(image):
    return color.rgb2gray(image)

def blur(img):
    img = cv2.bilateralFilter(img.astype(np.float32), 15, 80, 80)
    return img

def replace_pixel(binary, original): 
    blur_img = cv2.GaussianBlur(original, (15, 15), 0)
    binary = binary.astype(np.uint8)
    out = np.zeros(binary.shape)
    out[binary == 1] = original[binary == 1]
    out[binary == 0] = blur_img[binary == 0]

    return out

from skimage.filters import threshold_otsu
def binary_otsu(img):
    thresh = threshold_otsu(img)
    binary = img <= thresh
    return binary
