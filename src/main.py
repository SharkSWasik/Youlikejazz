import preprocessing
import postprocessing
from preprocessing import to_gray
from preprocessing import to_lba
from preprocessing import blur
from preprocessing import binary_otsu
from preprocessing import replace_pixel
from skimage.morphology import remove_small_objects
from postprocessing import detect
from postprocessing import to_csv
import argparse
import os
import skimage.io

from skimage import exposure
import scipy
from skimage.morphology import skeletonize

def get_skelet(image):
    gray_image = to_gray(image)

    blurred = blur(gray_image)

    otsu = binary_otsu(blurred)

    remove_small_objects(otsu, min_size=100000, connectivity=100, in_place=True)

    dilated = skimage.morphology.binary_dilation(otsu, skimage.morphology.disk(5))

    erosion = skimage.morphology.binary_erosion(dilated, skimage.morphology.disk(3))

    change_pixel = replace_pixel(erosion, gray_image)

    gaussian_filter = scipy.ndimage.gaussian_filter(change_pixel, sigma=1.0)

    otsu = binary_otsu(gaussian_filter)

    remove_small_objects(otsu, min_size=100000, connectivity=10, in_place=True)

    dilated = skimage.morphology.binary_dilation(otsu, skimage.morphology.disk(20))

    erosion = skimage.morphology.binary_erosion(dilated, skimage.morphology.disk(3))

    skelet = skeletonize(erosion, method = 'zhang')

    return skelet

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='beewing')
    parser.add_argument('--dst', type=str, default="Data/", help='csv destination path')
    parser.add_argument('--src', type=str, default="RESULT/", help='images source path')
    args = parser.parse_args()

    if not os.path.exists(args.dst):
        try:
            os.makedirs(args.dst)
        except:
            print("fail to create directory")
            sys.exit()

    images_path = [im for im in sorted(os.listdir(args.src)) if im[-3:] == "jpg"]
    images = [skimage.io.imread(args.src + im) for im in sorted(os.listdir(args.src)) if im[-3:] == "jpg"]


    for i in range(len(images)):
        skelet = get_skelet(images[i])
        detection = detect(skelet)
        to_csv(detection, args.dst + images_path[i][:-4])
