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
    plt.pause(0.0015)
    pic = imageio.imread(img)
    
    axs.set_xlabel(img, fontsize=8)
    
    if pic.ndim < 3 :
        axs.imshow(pic, cmap=plt.get_cmap('gray'))
    else:
        axs.imshow(pic)
       
    plt.pause(0.0015)  
        

def disp(img1, img2):
    plt.ion()
    print ("Are the displayed files indeed duplicates?")
    
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,10))
    fig.canvas.set_window_title('Potential Duplicates')
    
    checkGrayscaleAndShow(axs[0], img1)

    checkGrayscaleAndShow(axs[1], img2)
    
    plt.grid(b=False)
    plt.show()
    
    answr = input() 
    
    plt.pause(0.0005)
    fig.clf()
    plt.close()
    plt.pause(0.0005)
    
    return(answr)
