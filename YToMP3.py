import os
import time
from pytube import YouTube

# Get the path to the .txt file (you named it in the previous step)
file_path = os.path.join(os.getcwd(), "v_links.txt")

# Open the file in read mode
with open(file_path, "r") as f:

    # Read the lines of the file
    video_urls = f.readlines()

# Create the directory for the downloaded MP3 files (for example on disk D)
mp3s_dir = os.path.join("D:")

# Check if the directory exists
if not os.path.exists(mp3s_dir):
  # Create the directory if it doesn't exist
  os.mkdir(mp3s_dir)

# Download the videos and convert them to MP3 files
for video_url in video_urls:
  try:
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="mp3s_dir")
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
  except Exception as e:
    # Throw an exception if an error occurs
    print(e)
    continue


# Print a message to indicate that the download is complete
print("Download complete!")