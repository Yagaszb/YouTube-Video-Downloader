import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import os

selected_directory = ""

def choose_directory():
    global selected_directory  
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        directory_label.config(text="Selected directory: " + selected_directory)
    else:
        directory_label.config(text="No directory selected")

def download_video():
    status_label.config(text="Started downloading video...")
    url = url_entry.get()
    if url and selected_directory:  
        try:
            yt = YouTube(url)
            if download_audio_var.get():
                stream = yt.streams.filter(only_audio=True).first()
            else:
                stream = yt.streams.get_highest_resolution()

            stream.download(output_path=selected_directory)
            status_label.config(text="Download completed successfully!")
            messagebox.showinfo("Success", "Download completed successfully!")
        except Exception as e:
            status_label.config(text="Error: " + str(e))
    else:
        status_label.config(text="Please enter a valid YouTube URL and select a directory")

app = tk.Tk()
app.title("YouTube Video Downloader")

madeby_label = tk.Label(app, text="Made by Yagi")
madeby_label.pack()

choose_button = tk.Button(app, text="Choose Directory", command=choose_directory)
choose_button.pack()

directory_label = tk.Label(app, text="")
directory_label.pack()

url_label = tk.Label(app, text="Enter YouTube Video URL:")
url_label.pack()

url_entry = tk.Entry(app, width=40)
url_entry.pack()

download_audio_var = tk.BooleanVar()  
audio_checkbox = tk.Checkbutton(app, text="Download Audio Only", variable=download_audio_var)
audio_checkbox.pack()

download_button = tk.Button(app, text="Download Video", command=download_video)
download_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
