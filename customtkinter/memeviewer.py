import customtkinter as ctk
import tkinter as tk
from tkinter import PhotoImage

# Constants
GIF_PATH = 'C:\\Users\\prach\\Downloads\\asdasdasd\\customtkinter\\natural-symmetry.gif'
FRAME_INTERVAL = 0  # milliseconds
WINDOW_SIZE = "500x300"

def update_image(index=0):
    try:
        frame = PhotoImage(file=GIF_PATH, format=f"gif -index {index}")
        gif_label.configure(image=frame)
        gif_label.image = frame
        index += 1
    except tk.TclError:
        index = 0
    finally:
        app.after(FRAME_INTERVAL, update_image, index)

def main():
    global app, gif_label
    app = ctk.CTk()
    app.title("Display Animated GIF")
    app.geometry(WINDOW_SIZE)

    text_label = ctk.CTkLabel(app, text="Here is an animated GIF below:")
    text_label.pack(pady=(10, 5))

    gif_label = tk.Label(app)
    gif_label.pack()
    frame = PhotoImage(file=GIF_PATH, format="gif -index 0")
    gif_label.configure(image=frame)
    gif_label.image = frame

    update_image()
    app.mainloop()

if __name__ == "__main__":
    main()
