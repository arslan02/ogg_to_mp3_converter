from pydub import AudioSegment
import os
import sys

def convert_ogg_to_mp3(ogg_file: str):
  # Load the OGG file
  sound = AudioSegment.from_file(ogg_file)
  # Export it as an MP3 file
  sound.export(ogg_file.removesuffix(".ogg") + ".mp3", format="mp3", bitrate="128k")

def go_through_dir(dir_path: str):
   print("Going through " + dir_path)
   for entry in os.scandir(dir_path):
      if entry.is_dir():
         go_through_dir(entry.path)
      else:
         if entry.is_file() and entry.name.endswith(".ogg"):
            convert_ogg_to_mp3(entry.path)

path = sys.argv[1]
go_through_dir(path)

