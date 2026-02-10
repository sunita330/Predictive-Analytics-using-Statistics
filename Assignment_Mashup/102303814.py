import sys
import os
from yt_dlp import YoutubeDL
from moviepy import VideoFileClip, concatenate_audioclips

def download_videos(singer, n):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'quiet': True
    }
    query = f"ytsearch{n}:{singer} song"
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([query])

def process_videos(duration):
    clips = []
    for file in os.listdir("videos"):
        if file.endswith(".mp4"):
            video = VideoFileClip(os.path.join("videos", file))
            audio = video.audio.subclipped(0, duration)
            clips.append(audio)
    return clips

def merge_audios(clips, output):
    final_audio = concatenate_audioclips(clips)
    final_audio.write_audiofile(output)

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python <RollNumber>.py <SingerName> <NoOfVideos> <Duration> <OutputFile>")
        sys.exit(1)

    singer = sys.argv[1]
    n = int(sys.argv[2])
    duration = int(sys.argv[3])
    output = sys.argv[4]

    if n <= 10 or duration <= 20:
        print("Error: Videos > 10 and duration > 20 required")
        sys.exit(1)

    os.makedirs("videos", exist_ok=True)

    download_videos(singer, n)
    clips = process_videos(duration)
    merge_audios(clips, output)

    print("Mashup created successfully!")
