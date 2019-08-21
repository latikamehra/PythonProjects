'''
Created on Aug 20, 2019

@author: latikamehra
'''

import matplotlib
import matplotlib.pyplot as plt
import imageio

def topfig(fig):
    pass


def checkGrayscaleAndShow(axs, img):
    plt.pause(0.0005)
    pic = imageio.imread(img)
    
    if pic.ndim < 3 :
        axs.imshow(pic, cmap=plt.get_cmap('gray'))
    else:
        axs.imshow(pic)
       
    plt.pause(0.0010)  
        

def disp(img1, img2):
    plt.ion()
    print ("Are the displayed files indeed duplicates?")
    
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,10))
    fig.canvas.set_window_title('Potential Duplicates')

    axs[0].set_xlabel(img1, fontsize=8)
    axs[1].set_xlabel(img2, fontsize=8)
    
    checkGrayscaleAndShow(axs[0], img1)

    checkGrayscaleAndShow(axs[1], img2)
    

    plt.show()
    
    answr = input() 
    
    plt.pause(0.0005)
    plt.close()
    plt.pause(0.0005)
    
    return(answr)
