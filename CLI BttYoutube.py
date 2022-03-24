from pytube import YouTube
import os
from pytube.cli import on_progress

while True :

  yt = YouTube(
     str(input("Enter the URL of the video you want to download: \n>> ")),on_progress_callback=on_progress)
  
  video = yt.streams.filter(only_audio=True).first()
  out_file = video.download(output_path=".")
  
  base, ext = os.path.splitext(out_file)
  print("wait for "+base)
  new_file = base + '.mp3'
  os.rename(out_file, new_file)
  
  print(yt.title + " has been successfully downloaded.")
