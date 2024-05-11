import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import requests

# Constants
IMAGE_API_URL = "https://picsum.photos/1600/1020"
UPDATE_INTERVAL = 5000  # milliseconds (5 seconds)
WINDOW_SIZE = "1600x1020"

def update_image():
    try:
        response = requests.get(IMAGE_API_URL)
        image_data = BytesIO(response.content)
        pil_image = Image.open(image_data)
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image  # Keep a reference!
    except Exception as e:
        print(f"Error fetching image: {e}")
    finally:
        app.after(UPDATE_INTERVAL, update_image)

def main():
    global app, image_label
    app = ctk.CTk()
    app.title("Random Image Viewer")
    app.geometry(WINDOW_SIZE)

    image_label = tk.Label(app)
    image_label.pack(fill=tk.BOTH, expand=True)

    update_image()  # Initial call to start the image updates
    app.mainloop()

if __name__ == "__main__":
    main()
