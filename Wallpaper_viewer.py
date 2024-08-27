from tkinter import *
from PIL import ImageTk, Image
import os

def rotate_image():
    global counter
    # Update the image on the label
    img_label.config(image=img_array[counter % len(img_array)])
    counter += 1

counter = 0  # Start from 0 to display the first image correctly
root = Tk()
root.title('Wallpaper viewer')
root.geometry('250x400')
root.configure(background='black')

# List all image files in the 'wallpaper' directory
files = [f for f in os.listdir('wallpaper') if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
img_array = []

for file in files:
    try:
        img = Image.open(os.path.join('wallpaper', file))
        resize_image = img.resize((200, 300))
        img_array.append(ImageTk.PhotoImage(resize_image))
    except Exception as e:
        print(f"Error loading image {file}: {e}")

# Ensure that img_array is not empty before creating the label
if img_array:
    img_label = Label(root, image=img_array[0])
    img_label.pack(pady=(15, 10))
    next_btn = Button(root, text='Next', bg='white', fg='black', width=28, height=2, command=rotate_image)
    next_btn.pack()
else:
    print("No images found in the 'wallpaper' directory.")

root.mainloop()
