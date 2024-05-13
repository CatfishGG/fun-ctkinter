import customtkinter as ctk
import requests
import json

# Set up the API key and base URL
API_KEY = "Your_API_Key_Here"
BASE_URL = "https://api.ipgeolocation.io/ipgeo"

# Function to fetch geolocation data
def fetch_geolocation(ip_address):
    params = {
        "apiKey": API_KEY,
        "ip": ip_address
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Function to update the display with geolocation data
def update_display():
    ip_address = ip_entry.get()
    data = fetch_geolocation(ip_address)
    formatted_data = json.dumps(data, indent=4)  # Pretty print the JSON
    result_text.delete('1.0', ctk.END)  # Clear the existing text
    result_text.insert(ctk.END, formatted_data)  # Insert new data

# Main window setup
app = ctk.CTk()
app.title("IP Geolocation Lookup")
app.geometry("500x600")

# Entry for IP address
ip_entry = ctk.CTkEntry(app, placeholder_text="Enter IP Address")
ip_entry.pack(pady=20, padx=20)

# Button to trigger geolocation lookup
fetch_button = ctk.CTkButton(app, text="Get Geolocation", command=update_display)
fetch_button.pack(pady=10)

# Textbox and Scrollbar setup
frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

result_text = ctk.CTkTextbox(frame, height=15, wrap="word")
result_text.pack(side="left", fill="both", expand=True)

scrollbar = ctk.CTkScrollbar(frame, command=result_text.yview)
scrollbar.pack(side="right", fill="y")

result_text.configure(yscrollcommand=scrollbar.set)

# Run the app
app.mainloop()
