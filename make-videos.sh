#!/bin/bash

set -e 

SCRIPT_DIR=$(dirname $(realpath $0))

for dir in ${SCRIPT_DIR}/*/
do
  builtin cd ${dir}
  video=$(basename ${dir})
  echo ${video}
  ffmpeg -framerate 24 -pattern_type glob -i '*.jpg' -loglevel quiet ../${video}.mp4
  builtin cd ../
done
