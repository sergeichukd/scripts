import sys
from pathlib import Path
from time import time_ns

import cv2
import numpy as np

SEPARATOR_WIDTH = 20

video_path_left = Path(sys.argv[1])
video_path_right = Path(sys.argv[2])

assert video_path_left.is_file(), f'Video does not exist: {video_path_left}'
assert video_path_right.is_file(), f'Video does not exist: {video_path_right}'

OUTPUR_DIR = Path('results') / f'{video_path_left.stem}__{video_path_right.stem}'
OUTPUR_DIR.mkdir(parents=True, exist_ok=True)

cap_left = cv2.VideoCapture(video_path_left.as_posix())
cap_right = cv2.VideoCapture(video_path_right.as_posix())
h0 = int(cap_left.get(cv2.CAP_PROP_FRAME_HEIGHT))
w0 = int(cap_left.get(cv2.CAP_PROP_FRAME_WIDTH))
h1 = int(cap_right.get(cv2.CAP_PROP_FRAME_HEIGHT))
w1 = int(cap_right.get(cv2.CAP_PROP_FRAME_WIDTH))
h_max = max(h0, h1)
result_hwc = h_max, w0 + SEPARATOR_WIDTH + w1, 3

total_frames = max(int(cap_left.get(cv2.CAP_PROP_FRAME_COUNT)), int(cap_right.get(cv2.CAP_PROP_FRAME_COUNT)))
frames_counter = 0

while True:
    success_left, frame_left = cap_left.read()  # bgr
    success_right, frame_right = cap_right.read()  # bgr
    if not success_left and not success_right:
        break
    result_frame = np.ones(result_hwc)
    if success_left:
        result_frame[:h0, :w0, :] = frame_left
    if success_right:
        result_frame[-h1:, -w1:, :] = frame_right
    result_frame[h0:h1, w0:w1, :] *= 255
    result_path = OUTPUR_DIR / f'{time_ns()}.jpg'
    cv2.imwrite(result_path.as_posix(), result_frame)
    if frames_counter % 25 == 0:
        print(f'{success_left} {success_right} | Frame {frames_counter} / {total_frames} | Write to {result_path}')
    frames_counter += 1

cap_left.release()
cap_right.release()
