#!/usr/bin/env python3
import os
from glob import glob

from PIL import Image

OUT_DIR_1 = os.path.join('.', 'skytemple_icons', 'hicolor')
FILE_SIZES = {
    '16x16': 16,
    '32x32': 32,
    '64x64': 64,
    '128x128': 128,
    '256x256': 256,
    '512x512': 512
}
OUT_DIR_2 = 'apps'

COLOR_MAP = {
    (0, 0, 0, 0): (0, 0, 0, 0),
    (211, 218, 227, 255): (0, 0, 0, 216),
    (138, 144, 155, 255): (0, 0, 0, 114),
    (94, 100, 113, 255): (0, 0, 0, 55),
}

for file_name in glob(os.path.join('.', 'source', '*.png')):
    print(file_name)
    img: Image.Image = Image.open(file_name).convert("RGBA")
    pixdata = img.load()
    for y in range(0, img.size[1]):
        for x in range(0, img.size[0]):
            if pixdata[x, y] in COLOR_MAP:
                pixdata[x, y] = COLOR_MAP[pixdata[x, y]]
            else:
                raise ValueError(f"Unknown color at {x},{y}.")

    for dirname, size in FILE_SIZES.items():
        os.makedirs(os.path.join(OUT_DIR_1, dirname, OUT_DIR_2), exist_ok=True)
        out_filename = os.path.join(
            OUT_DIR_1, dirname, OUT_DIR_2, os.path.basename(file_name).replace('.png', '.symbolic.png')
        )
        out_img = img.resize((size, size), resample=Image.NEAREST)
        print(f">> {out_filename}")
        out_img.save(out_filename)
