from flask import Flask, render_template, request
import os
import zipfile
import smtplib
from email.message import EmailMessage

from yt_dlp import YoutubeDL
from moviepy import VideoFileClip, concatenate_audioclips

app = Flask(__name__)

# -------- Mashup Logic --------
def create_mashup(singer, n, duration, output):
    os.makedirs("videos", exist_ok=True)

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'quiet': True
    }

    query = f"ytsearch{n}:{singer} song"
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([query])

    clips = []
    for file in os.listdir("videos"):
        if file.endswith(".mp4"):
            video = VideoFileClip(os.path.join("videos", file))
            audio = video.audio.subclipped(0, duration)
            clips.append(audio)

    final_audio = concatenate_audioclips(clips)
    final_audio.write_audiofile(output)

# -------- Email Function --------
def send_email(receiver, zip_file):
    sender = "sunitajogpal614@gmail.com"
    password = "ddbv cfuc emyd ulvm"   

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Your mashup file is attached.")

    with open(zip_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="zip",
            filename=zip_file
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

# -------- Routes --------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form["singer"]
        videos = int(request.form["videos"])
        duration = int(request.form["duration"])
        email = request.form["email"]

        output_audio = "output.mp3"
        zip_name = "mashup.zip"

        create_mashup(singer, videos, duration, output_audio)

        with zipfile.ZipFile(zip_name, "w") as zipf:
            zipf.write(output_audio)

        send_email(email, zip_name)

        return "Mashup created and sent to your email successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run()

