'''
Created on Aug 20, 2019

@author: latikamehra
'''

import matplotlib
import matplotlib.pyplot as plt
import imageio




def topfig(fig):
    pass

def disp(img1, img2):
    plt.ion()
    print ("Are the displayed files indeed duplicates?")
    
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10,10))
    fig.canvas.set_window_title('Potential Duplicates')

    axs[0].set_xlabel(img1, fontsize=8)
    axs[1].set_xlabel(img2, fontsize=8)
    
    pic1 = imageio.imread(img1)
    pic2 = imageio.imread(img2)
    
    plt.pause(0.0005)
    axs[0].imshow(pic1)
    plt.pause(0.0010) 
    axs[1].imshow(pic2)
    plt.pause(0.0010) 
    

    plt.show()
    
    answr = input() 
    
    plt.pause(0.0005)
    plt.close()
    plt.pause(0.0005)
    
    return(answr)
