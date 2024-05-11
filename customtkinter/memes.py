import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import tempfile
import os

def fetch_meme():
    url = "https://programming-memes-images.p.rapidapi.com/v1/memes"
    headers = {
        "X-RapidAPI-Key": "8b5b66c116mshe989a6cb460bb2cp17145fjsn02130f2343b4",
        "X-RapidAPI-Host": "programming-memes-images.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    memes = response.json()
    if memes:
        meme_url = memes[0]['image']
        print("Fetching meme from:", meme_url)
        response = requests.get(meme_url)
        if meme_url.endswith('.gif'):
            # Handle GIFs
            temp_file, temp_path = tempfile.mkstemp(suffix='.gif')
            with open(temp_path, 'wb') as f:
                f.write(response.content)
            animate_gif(temp_path)
        else:
            # Handle static images
            img = Image.open(BytesIO(response.content))
            img = img.resize((300, 300), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            meme_label.configure(image=img_tk)
            meme_label.image = img_tk
    app.after(10000, fetch_meme)  # Fetch every 10 seconds

def animate_gif(path, index=0):
    try:
        frame = tk.PhotoImage(file=path, format=f"gif -index {index}")
        gif_label.configure(image=frame)
        gif_label.image = frame  # Keep a reference!
        index += 1
    except tk.TclError:
        index = 0  # Reset to the first frame
    finally:
        app.after(50, animate_gif, path, index)  # Adjust the delay here to change speed

app = ctk.CTk()
app.title("Meme Display")
app.geometry("320x350")

meme_label = tk.Label(app)  # Use Tkinter Label for GIFs
meme_label.pack(pady=20)

text_label = ctk.CTkLabel(app, text="Enjoy the memes!")
text_label.pack(pady=(10, 5))

gif_label = tk.Label(app)  # Separate label for GIFs
gif_label.pack()

fetch_meme()

app.mainloop()