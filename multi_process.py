import multiporcessing as mp
import os
from color_character import colorful_Chinese



def multiprocess_colorfulChinese():
    return

cmap_list = []
font_list = []
character_list = []

pool = mp.Pool(10)

for cmap in cmap_list:
    for font in font_list:
        pool.apply_async(colorful_Chinese, args=(font, cmap))


