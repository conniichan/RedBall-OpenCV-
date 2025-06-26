import cv2 as cv
import os 
import matplotlib.pyplot as plt

def readAndWriteSinglePixel(): #this is defining a function 
    root = os.getcwd() #get current working directory
    imgPath = os.path.join(root, 'images','redball.jpeg') #create path to image
    img = cv.imread(imgPath) #reads the image from the path 

    if img is None: #checks if the image was read correctly
        print('Image not found') 
        return
    else :
        print('Image found')
    

    
    
    cv.imshow('redball', img) #displays the image in a window
    cv.waitKey(0) #keeps the window open until a key is pressed
    cv.destroyAllWindows() #emnsures window is closed after key pressed and 
    #any resources used are released

if  __name__ == "__main__":
    readAndWriteSinglePixel()
