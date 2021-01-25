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

for file_name in glob(os.path.join('.', 'source_illust', '*.png')):
    name = os.path.basename(file_name)[:-4]
    print(name)
    img: Image.Image = Image.open(file_name).convert("RGBA")

    for dirname, size in FILE_SIZES.items():
        os.makedirs(os.path.join(OUT_DIR_1, dirname, OUT_DIR_2), exist_ok=True)
        out_filename = os.path.join(
            OUT_DIR_1, dirname, OUT_DIR_2, f'skytemple-illust-{name}.png'
        )
        out_img = img.copy()
        out_img.thumbnail((size, size))
        print(f">> {out_filename}")
        out_img.save(out_filename)
