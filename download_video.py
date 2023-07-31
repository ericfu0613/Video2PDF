import subprocess
import os
import multiprocessing


def download_video(url):
    video_format = "18"  # This will download mp4 video in 640x360 resolution
	@@ -20,16 +23,20 @@ def download_video(url):
    video_title = video_title.decode("utf-8").strip()
    video_filename = f"{video_title}.mp4"

    print(video_filename)
    # Call the generate_srt function
    generate_srt(video_filename)


    return video_filename

def generate_srt(video_filename):
    # Generate srt using whisper-ctranslate2
    num_cores = multiprocessing.cpu_count()
    print("This notebook has access to {} cores".format(num_cores))
    command_srt = [
        "whisper-ctranslate2",
        "--threads", str(num_cores) ,
        "--output_format", "srt",
        video_filename,
    ]

    # Execute the whisper-ctranslate2 command
    subprocess.run(command_srt, check=True)
