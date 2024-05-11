import customtkinter as ctk
import tkinter as tk
from tkinter import simpledialog
import requests

def translate_text():
    api_url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    source_text = text_input.get("1.0", tk.END).strip()
    if source_text == "" or source_text == "Enter text to translate":
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "Please enter some text to translate.")
        return

    translation_direction = language_selection.get()
    source, target = translation_direction.split(" to ")

    data = {
        "q": source_text,
        "source": source,
        "target": target,
        "format": "text"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "8b5b66c116mshe989a6cb460bb2cp17145fjsn02130f2343b4",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    try:
        response = requests.post(api_url, data=data, headers=headers)
        if response.status_code == 200:
            translated_text = response.json()['data']['translations'][0]['translatedText']
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, translated_text)
        else:
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, f"Failed to translate. Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, f"An error occurred: {e}")

def main():
    global text_input, text_output, language_selection
    app = ctk.CTk()
    app.title("Simple Translator")
    app.geometry("400x300")

    text_input = ctk.CTkTextbox(app, height=10)
    text_input.insert("1.0", "Enter text to translate")
    text_input.pack(pady=20, padx=20, fill="both", expand=True)

    language_selection = ctk.CTkComboBox(app, values=["en to es", "es to en"])
    language_selection.set("en to es")  # default selection
    language_selection.pack(pady=10)

    translate_button = ctk.CTkButton(app, text="Translate", command=translate_text)
    translate_button.pack(pady=10)

    text_output = ctk.CTkTextbox(app, height=10, state="normal")
    text_output.pack(pady=20, padx=20, fill="both", expand=True)

    app.mainloop()

if __name__ == "__main__":
    main()
