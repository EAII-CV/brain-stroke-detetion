
# import requered packages
import os
import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot,image
import glob

path = glob.glob('F:/theises/proposal/Dataset/Organized Dataset/Ischemic Stroke/0538050/Mask/*.png')
# creating loop that iterate for each mask images in the folder
for i in path:
    print(i)
    img=cv2.imread(i)
    # multiplication of float values by 255 to obtain Uint8 pixel value of images
    img=img*255
    cv2.imwrite(i,img)