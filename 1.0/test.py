from PIL import Image
from Image import Image
from Kernels import Kernels
import glob
import numpy as np
import cv2


imob=Image(cv2.imread('part.png',0))
imob.size()
imob.smoothing()
kernel=Kernels(5,5)
kernel.create()

blur_img1=imob.bilateral_img
for i in range(0,kernel.count):
    blur_img=blur_img1
    for j in range(0,1):
        blur_img = cv2.filter2D(blur_img, -1,kernel.kernels[i])
    img_name='image/kernel'+str(i)+'.png'
    cv2.imwrite(img_name,blur_img)

