import subprocess

input_file = "inputvideo.mkv"
output_file = "output_video.mp4"

subprocess.run([
    "ffmpeg",
    "-i", input_file,
    "-c", "copy",
    output_file
])

print("Done")
