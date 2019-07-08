from PIL import Image
from Image import Image
from Kernels import Kernels
import glob
import numpy as np
import cv2

def averagePixelLevel(img,x,y,img_M,img_N):
    M,N=box.shape
    avg=0.0
    x0=x-int(M/2)
    y0=y-int(N/2)
    pixel_num=0
    for i in range(0,M):
        x1=x0+i
        for j in range(0,N):
            y1=y0+j
            if x1<0 or y1<0 or x1>=img_M or y1>=img_N:
               continue
            avg+=img[x1][y1]
            pixel_num+=1
    avg=avg/pixel_num
    return avg
def whichKernel(index):
    for i in range(0,kernel.n):
        return 0
def check0(index,x,y):
    

    if (x-box_Width)<0 or (y-box_Width)<0 or (x+box_Width)>imob.M or (y+box_Width)>imob.N : # can not be edge pixel
       return 1
    x0=x1=x2=x
    y0=y1=y2=y
    x2=x2+int(box_Width/2)
    y2=y2-int(box_Width/2)
    num0=num1=num2=0
    for i in range(0,box_Width):
        pixLevel0=imob.filtered_images[index][x][y]-imob.filtered_images[index][x0][y0]
        pixLevel1=imob.filtered_images[index][x][y]-imob.filtered_images[index][x1][y1]
        pixLevel2=imob.filtered_images[index][x][y]-imob.filtered_images[index][x2][y2]
        if pixLevel0>=-box_Range and pixLevel0<=box_Range:
           num0+=1
        if pixLevel1>=-box_Range and pixLevel1<=box_Range:
           num1+=1
        if pixLevel2>=-box_Range and pixLevel2<=box_Range:
           num2+=1
        x0+=1
        y0-=1
        x1-=1
        y1+=1
        x2-=1
        y2+=1
    if num0>=box_Val or num1>=box_Val or num2>=box_Val: # can not be edge pixel
       return 1
    else:
       return 0 # edge pixel
def check1(index,x,y):
   

    if (x-box_Width)<0  or (x+box_Width)>imob.M : # can not be edge pixel
       return 1
    x0=x1=x2=x
    y0=y1=y2=y
    x2=x2+int(box_Width/2)
    y2=y2
    num0=num1=num2=0
    for i in range(0,box_Width):
        pixLevel0=imob.filtered_images[index][x][y]-imob.filtered_images[index][x0][y0]
        pixLevel1=imob.filtered_images[index][x][y]-imob.filtered_images[index][x1][y1]
        pixLevel2=imob.filtered_images[index][x][y]-imob.filtered_images[index][x2][y2]
        if pixLevel0>=-box_Range and pixLevel0<=box_Range:
           num0+=1
        if pixLevel1>=-box_Range and pixLevel1<=box_Range:
           num1+=1
        if pixLevel2>=-box_Range and pixLevel2<=box_Range:
           num2+=1
        x0-=1
        x1+=1
        x2-=1
    if num0>=box_Val or num1>=box_Val or num2>=box_Val: # can not be edge pixel
       return 1
    else:
       return 0 # edge pixel
def check2(index,x,y):
    

    if (x-box_Width)<0 or (y-box_Width)<0 or (x+box_Width)>imob.M or (y+box_Width)>imob.N : # can not be edge pixel
       return 1
    x0=x1=x2=x
    y0=y1=y2=y
    x2=x2+int(box_Width/2)
    y2=y2+int(box_Width/2)
    num0=num1=num2=0
    for i in range(0,box_Width):
        pixLevel0=imob.filtered_images[index][x][y]-imob.filtered_images[index][x0][y0]
        pixLevel1=imob.filtered_images[index][x][y]-imob.filtered_images[index][x1][y1]
        pixLevel2=imob.filtered_images[index][x][y]-imob.filtered_images[index][x2][y2]
        if pixLevel0>=-box_Range and pixLevel0<=box_Range:
           num0+=1
        if pixLevel1>=-box_Range and pixLevel1<=box_Range:
           num1+=1
        if pixLevel2>=-box_Range and pixLevel2<=box_Range:
           num2+=1
        x0-=1
        y0-=1
        x1+=1
        y1+=1
        x2-=1
        y2-=1
    if num0>=box_Val or num1>=box_Val or num2>=box_Val: # can not be edge pixel
       return 1
    else:
       return 0 # edge pixel
def check3(index,x,y):
    

    if  (y-box_Width)<0 or (y+box_Width)>imob.N : # can not be edge pixel
       return 1
    x0=x1=x2=x
    y0=y1=y2=y
    x2=x2
    y2=y2+int(box_Width/2)
    num0=num1=num2=0
    for i in range(0,box_Width):
        pixLevel0=imob.filtered_images[index][x][y]-imob.filtered_images[index][x0][y0]
        pixLevel1=imob.filtered_images[index][x][y]-imob.filtered_images[index][x1][y1]
        pixLevel2=imob.filtered_images[index][x][y]-imob.filtered_images[index][x2][y2]
        if pixLevel0>=-box_Range and pixLevel0<=box_Range:
           num0+=1
        if pixLevel1>=-box_Range and pixLevel1<=box_Range:
           num1+=1
        if pixLevel2>=-box_Range and pixLevel2<=box_Range:
           num2+=1
        y0-=1
        y1+=1
        y2-=1
    if num0>=box_Val or num1>=box_Val or num2>=box_Val: # can not be edge pixel
       return 1
    else:
       return 0 # edge pixel
def checkWidth(index,x,y):#
    #print(index,"-",kernel.hash[index])
    if(kernel.hash[index]==0): 
        return check0(index,x,y)

    elif(kernel.hash[index]==1):
        return check3(index,x,y)

    elif(kernel.hash[index]==2):
        return check2(index,x,y)
    else:
        return check1(index,x,y)
     
    
def check(img,x,y,pixel_Val,step):
    '''
    we can determine a missing edge pixel (x,y) through this method.

    '''
    if step==1:
       return 1
    pixel_level=255.0 #max value of a pixel
    index=0           # by index we can know which kernel is usefull  for that pixel 
    for i in range(0,kernel.count): #this loop determines the lowest value of the pixel (x,y) from imgages that were created using different  Kernels and the Kernel  
        if imob.filtered_images[i][x][y]<pixel_level:
           pixel_level=imob.filtered_images[i][x][y]
           index=i
    if  pixel_Val>pixel_level :# edge pixel if width is small otherwise not (missing pixel of an edge)
        return checkWidth(index,x,y)
    else:                      # can be edge pixel or not so check it with one dimenional matrix [right bottom missing pixels.. ] can be used gaussian_img or average image
        return 1
                       

def work(img,step):
    M,N=img.shape
    for i in range(0,M):
        for j in range(0,N):
            pixel_Level=img[i][j]
            if pixel_Level <= maxEdgeVal:
               avg=averagePixelLevel(img,i,j,M,N) 
               if  avg <=avgVal :
                   bin_img[i][j]=0
               else:
                   bin_img[i][j]=check(img,i,j,img[i][j],step)
                   #if bin_img[i][j]==0:
                     # print('0x')
            else:
               bin_img[i][j]=(check(img,i,j,img[i][j],step))
               #if bin_img[i][j]==0:
                  #print('0y')
    return 0
'''
def work(img):
    M,N=img.shape
    for i in range(0,M):
        for j in range(0,N):
            pixel_Level=img[i][j]
            if pixel_Level <= maxEdgeVal:
               avg=averagePixelLevel(img,i,j,M,N) 
               if  avg <=avgVal :
                   bin_img[i][j]=0
               else:
                   bin_img[i][j]=check(img,i,j,img[i][j])
            else:
               bin_img[i][j]=(check(img,i,j,img[i][j]))
    return 0

'''
def init():
    global imob,kernel,maxEdgeVal,avgVal,n,m,bin_img,box,box_Width,box_Val,box_Range
    box_Range=15
    box_Val=7
    box_Width=10
    img_path='part.png'
    n=m=15
    avgVal=240.0
    kernel=Kernels(n,m)
    kernel.create()
    imob=Image(cv2.imread(img_path,0))
    imob.size()
    imob.smoothing()
    maxEdgeVal=imob.maxEdgeVal(imob.bilateral_img,100,150)
    bin_img=np.ones((imob.M,imob.N),np.bool)
    box=np.ones((5,5),np.float);

def main():
    init()
    work(imob.bilateral_img,1)
    bin_img1=255*bin_img
    imob.images(bin_img1,kernel.kernels,kernel.count)
    work(bin_img1,2)
    cv2.imwrite('bin.png',255*bin_img)


main()
