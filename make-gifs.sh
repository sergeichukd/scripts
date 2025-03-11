#!/bin/bash

set -e 

SCRIPT_DIR=$(dirname $(realpath $0))

for dir in ${SCRIPT_DIR}/*/
do
  builtin cd ${dir}
  video=$(basename ${dir})
  echo ${video}
  ffmpeg -f image2 -framerate 25 -pattern_type glob -i '*.jpg' -vf scale=640x480 -loglevel quiet ../${video}.gif
  builtin cd ../
done
