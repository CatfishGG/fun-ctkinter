import customtkinter as ctk
import requests

# Set the API key and the base URL for the Amdoren API
API_KEY = " ENTER YOUR API KEY HERE "
BASE_URL = "https://www.amdoren.com/api/currency.php"

# Function to fetch the exchange rate
def fetch_exchange_rate(from_currency, to_currency, amount):
    params = {
        "api_key": API_KEY,
        "from": from_currency,
        "to": to_currency
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if data.get("error"):
        return "Error: " + data.get("error")
    return float(data.get("amount", 0)) * amount

# Function to update the result label
def update_result():
    from_currency = currency_from_combobox.get()
    to_currency = currency_to_combobox.get()
    amount = float(amount_entry.get()) if amount_entry.get() and amount_entry.get().isdigit() else 0
    if from_currency and to_currency and amount > 0:
        result = fetch_exchange_rate(from_currency, to_currency, amount)
        result_label.configure(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        result_label.configure(text="Please enter a valid amount.")

# Main window setup
app = ctk.CTk()
app.title("Currency Converter")
app.geometry("400x300")

# Entry for the amount to convert
amount_entry = ctk.CTkEntry(app, placeholder_text="Amount")
amount_entry.pack(pady=10)

# Dropdown for 'from' currency
currency_from_combobox = ctk.CTkComboBox(app, values=["USD", "EUR", "GBP", "INR", "JPY"])
currency_from_combobox.set("From Currency")  # Default display text
currency_from_combobox.pack(pady=10)

# Dropdown for 'to' currency
currency_to_combobox = ctk.CTkComboBox(app, values=["USD", "EUR", "GBP", "INR", "JPY"])
currency_to_combobox.set("To Currency")  # Default display text
currency_to_combobox.pack(pady=10)

# Button to fetch and display the exchange rate
fetch_button = ctk.CTkButton(app, text="Convert", command=update_result)
fetch_button.pack(pady=10)

# Label to display the result
result_label = ctk.CTkLabel(app, text="Conversion Result Will Appear Here")
result_label.pack(pady=20)

# Run the app
app.mainloop()
