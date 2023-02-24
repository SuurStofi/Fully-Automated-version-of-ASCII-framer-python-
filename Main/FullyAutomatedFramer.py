from PIL import Image
import cv2
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

# ASCII converter you're able to use converters you find, just paste them into current function
def turnascii(image_path):
    img = Image.open(image_path)

    width, height = img.size
    aspect_ratio = height / width
    new_width = 50
    new_height = 38  # aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    returnmessage = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            returnmessage = returnmessage + f"{r} {g} {b}A"
    return returnmessage + "N"


# creating a folder
def folder():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    new_folder_path = os.path.join(dir_path, "frames")
    os.makedirs(new_folder_path, exist_ok=True)


# Video Capture
root = tk.Tk()
root.withdraw()
mp4_path = filedialog.askopenfilename(title="Select mp4 file", filetypes=[("MP4 Files", "*.mp4")])
shutil.move(mp4_path, os.path.join(os.path.basename(mp4_path)))
vidcap = cv2.VideoCapture(os.path.join(os.path.basename(mp4_path)))
success, image = vidcap.read()
count = 0
while success:
    folder()
    cv2.imwrite(f"./frames/frame{count}.jpg", image)
    success, image = vidcap.read()
    print(f"Rendered frame: {count}")

    with open(f"frames.txt", "a+") as f:
        writemessage = turnascii(f"./frames/frame{count}.jpg")
        f.write(writemessage)

    count += 1
