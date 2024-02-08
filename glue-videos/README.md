# Script to join 2-х .mp4 videos

How to use:
```bash
# From dir: <current_prj>/glue-videos
python -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt

# Create joined frames. Joined frames are saved to results/<left_video_stem>__<right_video_stem>
python glue_frames.py <path_to_left_video>  <path_to_right_video>

# Create video from joined frames. Video is saved to results/<left_video_stem>__<right_video_stem>.mp4
./make-video.sh results/<left_video_stem>__<right_video_stem>
```

