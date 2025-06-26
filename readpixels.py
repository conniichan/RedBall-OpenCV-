import cv2 as cv
import os 
import matplotlib.pyplot as plt

def readAndWriteSinglePixel(): #this is defining a function 
    root = os.getcwd() #get current working directory
    imgPath = os.path.join(root, 'images','redball.jpeg') #create path to image
    img = cv.imread(imgPath) #reads the image from the path 
    RGBimg = cv.cvtColor(img, cv.COLOR_BGR2RGB) #converts BGR to RGB

    if img is None: #checks if the image was read correctly
        print('Image not found') 
        return
    else :
        print('Image found')
    

    plt.imshow(RGBimg)
    plt.waitforbuttonpress()
    plt.close('all')
    
    
if  __name__ == "__main__":
    readAndWriteSinglePixel()
