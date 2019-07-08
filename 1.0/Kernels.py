import numpy as np


class Kernels:
  def __init__(self,n,m):# constructor that takes kernels size
    self.n=n  # row
    self.m=m  #column
    self.hash=[0 for i in range(n+m-2)]
    self.count=0;
    self.kernels=np.zeros((n+m-2,n,m),np.float);
  def kerlen0(self):
    kernel=np.zeros((self.n,self.m),np.float);
    self.kernels[0]=kernel;
    for i in range(0,self.n):
        kernel[i][i]=1.0;
    self.kernels[self.count]=kernel/self.n;
    self.hash[self.count]=0
    self.count+=1


  def kerlen1(self):
    
    for i in range(1,int((self.n-1)/2)):
        kernel=np.zeros((self.n,self.m),np.float);
        num=int((self.n-1)/2-1)
        num1=int((num)/i)
        num2=2+num1+num
        k=0
        l=i
        j=1
        #print(i)
        while 1==1:
             kernel[k][l]=1.0
             #print(k,l)
             kernel[k+int((self.n-1)/2)][l+int((self.m-1)/2)-i]=1.0
             #print(k+int((self.n-1)/2)," ",l+int((self.m-1)/2)-i)
             if k==l and k==int((self.n-1)/2):
                break
             if k==int((self.n-1)/2):
               l=l+1 
             elif j%(i+1)==0:
               l=l+1
             else:
               k=k+1
             j=j+1
        self.kernels[self.count]=kernel/(num2*2-1)
        if (self.count<=int(int((self.n)/2)/2)):
           self.hash[self.count]=0
        else:
           self.hash[self.count]=1
        self.count+=1
             
        '''
        for j in range(1,num2+1):
            kernel[k][l]=1.0
            kernel[k+int((self.n-1)/2)][l+int((self.m-1)/2)-1]=1.0
            if j%(i+1)==0:
               l=l+1
            else:
               k=k+1
        return kernel
        '''    
            
            
    #return kernel#/(num2*2-1);

  def kerlen2(self):
    kernel=np.zeros((self.n,self.m),np.float);
    for i in range(0,self.n):
        kernel[i][int((self.m-1)/2)]=1.0;
    self.kernels[self.count]=kernel/self.n
    self.hash[self.count]=1
    self.count+=1
    
  def kerlen3(self):
    
    for i in range(1,int((self.n-1)/2)):
        kernel=np.zeros((self.n,self.m),np.float);
        num=int((self.n-1)/2-1)
        num1=int((num)/i)
        num2=2+num1+num
        k=0
        l=self.m-i-1
        j=1
        mx=int((self.m-1)/2);
        while 1==1:
             kernel[k][l]=1.0
             kernel[k+int((self.n-1)/2)][mx]=1.0
             #print(k+int((self.n-1)/2)," ",mx)
             if k==l and k==int((self.n-1)/2):
                break
             if k==int((self.n-1)/2):
               l=l-1
             elif j%(i+1)==0:
               l=l-1
               mx=mx-1
             else:
               k=k+1
             j=j+1
        self.kernels[self.count]=kernel/(num2*2-1)
        if self.count<=(int(int((self.n)/2)/2)+int(self.n/2)):
           self.hash[self.count]=2
        else:
           self.hash[self.count]=1
        self.count+=1
        '''
        for j in range(1,num2+1):
            kernel[k][l]=1.0
            kernel[k+int((self.n-1)/2)][l+int((self.m-1)/2)-1]=1.0
            if j%(i+1)==0:
               l=l+1
            else:
               k=k+1
        return kernel
        '''    
            
            
    #return kernel#/(num2*2-1);
  def kerlen4(self):
    kernel=np.zeros((self.n,self.m),np.float);
    for i in range(0,self.n):
        kernel[i][self.m-i-1]=1.0;
    self.kernels[self.count]=kernel/self.n
    self.hash[self.count]=2
    self.count+=1
  def kerlen5(self):
    for i in range(int((self.n-1)/2)+1,self.n-1):
        self.kernels[self.count]=self.transpose(self.kernels[i])
        if i<=(int(int((self.n)/2)/2)+int(self.n/2)):
           self.hash[self.count]=2
        else:
           self.hash[self.count]=3
        self.count+=1

  def kerlen6(self):
    kernel=np.zeros((self.n,self.m),np.float);
    for i in range(0,self.n):
        kernel[int((self.n-1)/2)][i]=1.0;
    self.kernels[self.count]=kernel/self.n
    self.hash[self.count]=3
    self.count+=1;

  def kerlen7(self):
    for i in range(1,int((self.n-1)/2)):
        self.kernels[self.count]=self.transpose(self.kernels[i])
        if (self.count<=int(int((self.n)/2)/2)):
           self.hash[self.count]=0
        else:
           self.hash[self.count]=3
        self.count+=1
                           
  def create(self):# all kernels are created here
     self.kerlen0();
     self.kerlen1();
     self.kerlen2();
     self.kerlen3();
     self.kerlen4();
     self.kerlen5();
     self.kerlen6();
     self.kerlen7();
   
  def transpose(self,mat):
    kernel=np.zeros((self.n,self.m),np.float)
    for i in range(0,self.n):
        for j in range(0,self.m):
            kernel[i][j]=mat[j][i]
    return kernel 
    
  def printf(self,kernel):
    for i in range(0,self.n):
        for j in range(0,self.m):
            print(kernel[i][j], end =" ")
        print(""); 
    
