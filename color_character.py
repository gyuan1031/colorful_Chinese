import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image
import os



class Colour_Chinese(object):

    def __init__(self, character_list,  cmap_size=600, scale=500, output_size=64):

        self.character_list = character_list
        self.cmap_size = cmap_size
        self.scale = scale
        self.output_size = output_size

        self.font_path = '/data1/gaoy/fz_resized_64/'
        self.cmap_path = './cmaps'
        self.out_path = './out'

    def Process(self, cmap_name, font_id):

        cma_path = os.path.join(self.cmap_path, cmap_name)
        img_cmap = Image.open(cma_path)
        img_cmap.convert('RGB')
        img_cmap = np.array(img_cmap)

        fon_path = os.path.join(self.font_path, str(font_id))

        out_p = os.path.join(self.out_path, str(font_id) )
        if not os.path.exists(out_p):
            os.mkdir(out_p)

        for character in character_list:
            cha_path = os.path.join(fon_path, character)
            img_cha = Image.open(cha_path)
            img_cha = img_cha.resize((500, 500))
            img_cha.convert('RGB')
            img_cha = np.array(img_cha)

            output = projection_to_character(img_cha, img_cmap)
            output = Image.fromarray(output)
            output.resize((64, 64))
            output.save(os.path.join(out_p, cmap_name.split('.')[0] + "_" + character))

    def projection_to_character(self, character, cmap, cmap_size=600, scale=500):

        blank = (character[..., 0] > 128) & (character[..., 1] > 128) & (character[..., 2] > 128)
        # output = np.zeros((scale, scale, 3))

        central = cmap_size / 2
        x, y = int(central - scale / 2), int(central - scale / 2)

        output = cmap[x:x + scale, y:y + scale, :]
        output[blank] = 255

        return output

def get_chalist():

    file1 = open("gb639.txt", "r")
    out = []
    for line in file1:
        out.append(line.strip())
    return out

cha_list = get_chalist()
print cha_list
obj = Colour_Chinese(cha_list)
colorful_Chinese()
