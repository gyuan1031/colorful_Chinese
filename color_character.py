import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image
import os

def projection_to_character(character, cmap, cmap_size=600, scale=500):

    blank = (character[...,0] > 128) & (character[...,1] > 128) & (character[...,2] > 128)
    output = np.zeros((scale, scale, 3))

    central = cmap_size/2
    x, y = int(central-scale/2), int(central-scale/2)

    output = cmap[x:x+scale, y:y+scale, :]
    output[blank] = 255
    
    return output
    


def colorful_Chinese():

    character_list = ['GB4271_R.jpg']
    cmap_list = ['Accent.jpg']

    character_path = '/data1/gaoy/fz_resized_64/0/'
    cmap_path = './cmaps'
    out_path = './out'

    for character in character_list:
        for cmap in cmap_list:
            cha_path = os.path.join(character_path, character)
            img_cha = Image.open(cha_path)
            img_cha = img_cha.resize((500, 500))
            img_cha.convert('RGB')
            img_cha = np.array(img_cha)            

            cma_path = os.path.join(cmap_path, cmap)
            img_cmap = Image.open(cma_path) 
            img_cmap.convert('RGB')
            img_cmap = np.array(img_cmap)

            output = projection_to_character(img_cha, img_cmap)
            output = Image.fromarray(output)
            output.resize((64, 64))
            output.save(os.path.join(out_path, character))



colorful_Chinese()
