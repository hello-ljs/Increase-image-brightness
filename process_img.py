#2019-04-10
# lixiang 

from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt
import cv2
import glob
import numpy as np

def raise_light(img,value,index):
    image = change_chanel(cv2.imread(img))
    gam= exposure.adjust_gamma(image, value)
    plt.imsave('results/'+str(index)+'.jpg',gam)

def change_chanel(image):
    (r, g, b)=cv2.split(image)
    image=cv2.merge([b,g,r])
    return (image)

def get_light(image):
    image=cv2.imread(image)
    image = cv2.resize(image,(28,28))
    return(np.mean(image))

def main():
    index=0
    light_threshold = 300
    for img in glob.glob('img/img3/*'):
       # relsut=
        if(get_light(img)<light_threshold):
            print('image needs to raise light,processing...')
            img=raise_light(img,0.4,index)
            index=index+1

if __name__ == '__main__':
    main()
