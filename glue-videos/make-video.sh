#!/bin/bash

set -e

dir=$1
# dir="results"
builtin cd ${dir}
video=$(basename ${dir})
echo ${video}
ffmpeg -framerate 24 -pattern_type glob -i '*.jpg' -loglevel quiet ../${video}.mp4
builtin cd ../
