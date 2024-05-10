from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

# Function to download a video from YouTube
def download_video(url, path):
    try:
        # Create a YouTube object with the provided URL
        yt = YouTube(url)
        
        # Filter available streams to get progressive mp4 streams
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        
        # Get the highest resolution stream
        highest_res_stream = streams.get_highest_resolution()
        
        # Download the video to the specified output path
        highest_res_stream.download(output_path=path)
        
        print("Video downloaded Successfully!")
        
    except Exception as e:
        print(e)

# Function to open a file dialog for selecting a directory
def open_file_dialog():
    # Open a file dialog for selecting a directory
    folder = filedialog.askdirectory()
    
    if folder:
        print(f"Selected folder: {folder}")
    
    return folder

# Main block of the code
if __name__ == "__main__":
    # Create a Tkinter root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to input the YouTube video URL to download
    video_url = input("Enter the Youtube video URL to download: ")
    
    # Open a file dialog for selecting the directory to save the video
    save_dir = open_file_dialog()

    # If no directory is selected, print an error message
    if not save_dir:
        print("Invalid Location!")
    else:
        # If a valid directory is selected, initiate the download process
        print("Download Started....")
        download_video(video_url, save_dir)