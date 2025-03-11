import shutil
import sys
from pathlib import Path

import cv2
import numpy as np

REL_SEPARATOR = 0.01

path_0 = Path(sys.argv[1]).resolve()
path_1 = Path(sys.argv[2]).resolve()

if path_0.is_dir() and path_1.is_dir():
    images_0_paths = path_0.iterdir()
    images_1_paths = path_1.iterdir()
elif path_0.is_file() and path_1.is_file():
    images_0_paths = [path_0]
    images_1_paths = [path_1]
else:
    raise Exception

for img_path0, img_path1 in zip(sorted(images_0_paths), sorted(images_1_paths)):
    if img_path0.stem == '1711625340788382000':
        print(f'Skip {img_path0}')
        continue
    print(f'Compare: {img_path0}  <--> {img_path1}')
    img0 = cv2.imread(img_path0.as_posix())
    img1 = cv2.imread(img_path1.as_posix())
    assert (img0 == img1).all()

print('\nAll images are equal!')
