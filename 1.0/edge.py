from PIL import Image
from Image import Image
from Kernels import Kernels
import glob
import numpy as np
import cv2

def printf(kernel,n,m):
    for i in range(0,n):
        for j in range(0,m):
            print(kernel[i][j], end =" ")
        print(""); 
  

imob=Image(cv2.imread('map/part.png',0))
imob.size()
imob.smoothing()
blur_filter2 = np.zeros((15,15),np.float);
for i in range (0,15):
    for j in range (0,15):
        if j==i:
           blur_filter2[i][j]=1.0
blur_filter2=blur_filter2/15.0
printf(blur_filter2,15,15)
blur_img=imob.bilateral_img
for i in range(0,1):
    blur_img = cv2.filter2D(blur_img, -1, blur_filter2)
   
cv2.imwrite("bla.png",blur_img)
'''
imob.smoothing()
eVal=imob.maxEdgeVal(imob.bilateral_img,20,150)
print("Val=",eVal)
bin_img=imob.getImage(imob._img,eVal)
imob.draw(imob.blur_img)
#imob.draw(cv2.imread('map/part.png',0))

img=cv2.imread('map/part.png',0);
M, N = img.shape
print('M=',M,"N=",N) 
bin_img=np.zeros((M,N),np.uint8)

for i in range(1, M-1):
        for j in range(1, N-1):
           bin_img[i][j]=img[i][j]
cv2.imwrite("black_m.png",cv2.medianBlur(img,3))
'''
