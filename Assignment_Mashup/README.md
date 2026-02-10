---

```md
# Assignment 6 – Mashup Application (Program 1 & Program 2)

## 📌 Objective
The objective of this assignment is to design and implement a **Mashup system** using Python that:
- Downloads YouTube videos based on a singer name
- Extracts and trims audio clips
- Merges them into a single mashup file
- Provides results via:
  - **Program 1:** Command Line Interface
  - **Program 2:** Web Application with Email delivery

---

## 🛠️ Technologies Used
- Python 3.13
- yt-dlp (YouTube video downloader)
- MoviePy (audio extraction, trimming, merging)
- FFmpeg (multimedia backend)
- Flask (web framework)
- SMTP (Gmail) for email delivery
- HTML (frontend form)

All libraries are open-source and available via PyPI.

---

## 📂 Project Structure
```

Assignment6_Mashup/
│
├── 102303814.py          # Program 1 – CLI Mashup
├── app.py                # Program 2 – Flask Web App
├── templates/
│   └── index.html        # Web interface
├── videos/               # Downloaded videos (generated at runtime)
├── output.mp3            # Mashup audio (generated)
└── mashup.zip             # Zipped output (generated)

```

Generated files are not committed to GitHub.

---

# 🔹 Program 1 – Command Line Mashup

## 📄 File
```

102303814.py

````

## 📘 Description
This program implements a **command-line based mashup generator**.  
It accepts singer name, number of videos, duration of each clip, and output file name as input.  
The program downloads videos, extracts and trims audio, and merges all clips into a single MP3 file.

---

## ▶️ How to Run Program 1

### 1️⃣ Install Dependencies
```bash
pip install yt-dlp moviepy
````

(FFmpeg must be installed and added to system PATH.)

---

### 2️⃣ Run the Program

```bash
python 102303814.py "Sharry Mann" 20 30 output.mp3
```

### 🔹 Parameters

| Argument    | Description                        |
| ----------- | ---------------------------------- |
| Singer Name | Name of the singer                 |
| 20          | Number of videos (>10)             |
| 30          | Duration per clip in seconds (>20) |
| output.mp3  | Output mashup file                 |

---

## ✅ Output (Program 1)

* `output.mp3` – Final merged mashup audio

---

# 🔹 Program 2 – Web Application Mashup

## 📄 Files

```
app.py
templates/index.html
```

## 📘 Description

Program 2 is a **Flask-based web application** that provides a graphical interface for mashup generation.

Users provide:

* Singer name
* Number of videos
* Duration per video
* Email ID

The system:

1. Downloads videos using yt-dlp
2. Extracts and trims audio using MoviePy
3. Merges audio into a single MP3 file
4. Compresses output into a ZIP file
5. Sends the ZIP file to the user via email

---

## ▶️ How to Run Program 2

### 1️⃣ Install Dependencies

```bash
pip install flask yt-dlp moviepy
```

---

### 2️⃣ Email Configuration

* Enable **2-Step Verification** on Gmail
* Generate a **Gmail App Password**
* Update credentials in `app.py`:

```python
sender = "your_email@gmail.com"
password = "your_app_password"
```

⚠️ App password is hidden before uploading to GitHub for security.

---

### 3️⃣ Run the Flask App

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🖥️ Web Form Inputs

* Singer Name (dynamic, e.g., Taylor Swift, Arijit Singh)
* Number of videos (>10)
* Duration per video (>20 seconds)
* Valid Email ID

---

## 📤 Output (Program 2)

* `output.mp3` – Mashup audio file
* `mashup.zip` – Zipped output
* ZIP file is emailed to the user

---

## ⚠️ Notes

* Flask is run in non-debug mode to avoid FFmpeg auto-reload issues on Windows.
* yt-dlp JavaScript runtime warnings can be safely ignored.
* Generated output files are excluded from GitHub to prevent plagiarism and storage overhead.

---

## 🧪 Tested Environment

* OS: Windows 11
* Python Version: 3.13 (64-bit)
* FFmpeg: Installed and added to PATH

---

## 📦 Submission Guidelines

### ✅ Files Uploaded to GitHub

* `102303814.py`
* `app.py`
* `templates/index.html`
* `README.md`

### ❌ Files Not Uploaded

* `output.mp3`
* `mashup.zip`
* `videos/`
* Email passwords / credentials

---

## 📝 Conclusion

This assignment successfully implements a complete Mashup system using Python.
It demonstrates command-line processing, multimedia handling, web development, and email integration.

Both **Program 1 (CLI)** and **Program 2 (Web Application)** fully satisfy the assignment requirements.

---

```

