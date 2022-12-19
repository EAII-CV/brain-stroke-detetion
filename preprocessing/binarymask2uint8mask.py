
import os
import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot,image
import glob

path = glob.glob('F:/theises/proposal/Dataset/Organized Dataset/Ischemic Stroke/0538050/Mask/*.png')
#print(img*255)
for i in path:
    print(i)
    img=cv2.imread(i)
    img=img*255
    cv2.imwrite(i,img)