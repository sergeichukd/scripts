# Extrack audio from video
ffmpeg -i sample.avi -q:a 0 -map a sample.mp3

# Convert audio
ffmpeg -i audio.wav -acodec libmp3lame audio.mp3
