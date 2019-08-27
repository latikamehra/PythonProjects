'''
Created on Aug 20, 2019

@author: latikamehra
'''


import matplotlib.pyplot as plt
import imageio

def topfig(fig):
    pass


def checkGrayscaleAndShow(axs, img, pauseTimeFactor=1):
    plt.pause(0.0020*pauseTimeFactor)
    axs.grid(False)
    pic = imageio.imread(img)
    
    axs.set_xlabel(img, fontsize=8)
    
    if pic.ndim < 3 :
        axs.imshow(pic, cmap=plt.get_cmap('gray'))
    else:
        axs.imshow(pic)
       
    plt.pause(0.0010*pauseTimeFactor)  
        

def disp(img1, img2, pauseTimeFactor=1):
    plt.ion()
    print ("Are the displayed files indeed duplicates?")
    
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,10))
    fig.canvas.set_window_title('Potential Duplicates')
    
    checkGrayscaleAndShow(axs[0], img1)

    checkGrayscaleAndShow(axs[1], img2, pauseTimeFactor=pauseTimeFactor)
    
    plt.grid(b=False)
    plt.show()
    
    plt.pause(0.0010*pauseTimeFactor)
    
    answr = input() 
    
    plt.pause(0.0005*pauseTimeFactor)
    fig.clf()
    plt.close()
    
    return(answr)
