import shutil
import sys
from pathlib import Path

import cv2
import numpy as np

REL_SEPARATOR = 0.01

path_0 = Path(sys.argv[1]).resolve()
path_1 = Path(sys.argv[2]).resolve()
out_dir = path_0.parent / f'{path_0.name}-vs-{path_1.name}'
if out_dir.is_dir():
    shutil.rmtree(out_dir)
out_dir.mkdir(parents=True)

if path_0.is_dir() and path_1.is_dir():
    images_0_paths = path_0.iterdir()
    images_1_paths = path_1.iterdir()
elif path_0.is_file() and path_1.is_file():
    images_0_paths = [path_0]
    images_1_paths = [path_1]
else:
    raise Exception

for img_path0, img_path1 in zip(sorted(images_0_paths), sorted(images_1_paths)):
    print(f'Compare: {img_path0}  <--> {img_path1}')
    img0 = cv2.imread(img_path0.as_posix())
    img1 = cv2.imread(img_path1.as_posix())
    h0, w0, c0 = img0.shape
    h1, w1, c1 = img1.shape
    h_max, w_max = (max(img0.shape[0], img1.shape[0]), max(img0.shape[1], img1.shape[1]))
    out_shape = (h_max, int(w_max * 2 * (1 + REL_SEPARATOR)), 3)
    result = np.ones(out_shape) * 255
    result[:h0, :w0, :] = img0
    result[:h1, -w1:, :] = img1
    result_path = out_dir / img_path0.name
    cv2.imwrite(result_path.as_posix(), result)
    print(f'Saved to {result_path}')

print(f'Results saved to: {result_path.parent}')
print('\nDONE!')
