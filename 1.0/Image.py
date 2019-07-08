import matplotlib.pyplot as plt
import cv2
import numpy as np
class Image:
  def __init__(self,img):# constructor that takes an image of the map 
    self.M,self.N=img.shape  # M= width of the image and N=height of the image
    self._img=img

  def size(self):# print the size of the raw image
    print("size=",self.M,"*",self.N)

  def smoothing(self):
    self.blur_img = cv2.blur(self._img,(9,9))
    self.gaussian_img = cv2.GaussianBlur(self._img,(5,5),0)
    self.median_img = cv2.medianBlur(self._img,5)
    self.bilateral_img=blur = cv2.bilateralFilter(self._img,9,75,75)#edges are  preserved

  def histogram(self,img):
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    return hist
  def maxEdgeVal(self,img,percentage,size):
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    n=0;
    for i in range(0,size+1):
        n+=hist[i]
    m=(n*percentage)/100
    n=0;
    for i in range(0,size+1):
        n+=hist[i]
        if n>=m:
           return i
    return -1
  def getImage(self,img,eVal):
    M,N=img.shape
    bin_img=np.ones((M,N),np.bool)
    for i in range(0,M):
        for j in range(0,N):
            if img[i][j]<=eVal:
               bin_img[i][j]=0
    return bin_img

  def draw(self,img):
    imgplot = plt.imshow(img)
    plt.show()

  def images(self,img,filters,count):
    self.filtered_images=np.zeros((count,self.M,self.N),np.float);
    for i in range(0,count):
        self.filtered_images[i]= cv2.filter2D(img, -1,filters[i])   
