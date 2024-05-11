import customtkinter as ctk
import ollama

app = ctk.CTk()
app.title("Chatbot using Ollama")
app.geometry("1000x600")  # Window size adjustment

def send_input():
    user_input = entry.get().strip()
    if user_input:  # Ensure non-empty input
        combined_history.configure(state='normal')
        combined_history.insert(ctk.END, "You: " + user_input + "\n")  # Log user input
        combined_history.see(ctk.END)  # Scroll to the bottom of the text box
        combined_history.configure(state='disabled')

        response = generate_response(user_input)

        response_history.configure(state='normal')
        response_history.delete('1.0', ctk.END)  # Clear previous responses
        response_history.insert(ctk.END, "Bot: " + response + "\n")  # Show new response
        response_history.see(ctk.END)  # Scroll to start of the response
        response_history.configure(state='disabled')

        entry.delete(0, 'end')  # Clear the input field

def generate_response(input_text):
    response = ollama.chat(
        model='llama2-uncensored',
        messages=[{'role': 'user', 'content': input_text}]
    )
    return response['message']['content']

# Frame for input history and input field
left_frame = ctk.CTkFrame(app)
left_frame.pack(side='left', fill='both', expand=True)

# Frame for responses
right_frame = ctk.CTkFrame(app)
right_frame.pack(side='right', fill='both', expand=True)

# Textbox for logging user inputs
combined_history = ctk.CTkTextbox(left_frame, state='disabled', yscrollcommand=True)
combined_history.pack(fill='both', expand=True, padx=20, pady=(10, 5))

# Textbox for showing bot responses
response_history = ctk.CTkTextbox(right_frame, state='normal', yscrollcommand=True)
response_history.pack(fill='both', expand=True, padx=20, pady=10)

# Input field and send button integrated at the bottom of the left frame
entry_frame = ctk.CTkFrame(left_frame)
entry_frame.pack(fill='x', side='bottom', padx=20, pady=(0, 10))
entry = ctk.CTkEntry(entry_frame, placeholder_text="Type your question here")
entry.pack(side='left', fill='x', expand=True)
send_button = ctk.CTkButton(entry_frame, text="Send", command=send_input)
send_button.pack(side='right')

app.mainloop()
