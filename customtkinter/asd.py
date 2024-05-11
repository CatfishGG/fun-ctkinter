import customtkinter as ctk
import ollama

app = ctk.CTk()
app.title("Chatbot using Ollama")
app.geometry("1000x600")  # Adjust window size

def send_input(event=None):
    user_input = combined_history.get("end-2c linestart", "end-1c").strip()
    if user_input.startswith("You: "):
        user_input = user_input[5:]  # Strip the prefix to get the actual input

    if user_input:  # Ensure non-empty input
        combined_history.configure(state='normal')
        combined_history.delete("end-2c linestart", "end-1c")  # Clear the user input line

        response = generate_response(user_input)
        
        combined_history.insert(ctk.END, "Bot: " + response + "\n")  # Display bot response
        combined_history.insert(ctk.END, "You: ")  # Reset for next input
        combined_history.see(ctk.END)  # Scroll to the new input line

def generate_response(input_text):
    response = ollama.chat(
        model='llama2-uncensored',
        messages=[{'role': 'user', 'content': input_text}]
    )
    return response['message']['content']

# Frame for combined input and log
left_frame = ctk.CTkFrame(app)
left_frame.pack(side='left', fill='both', expand=True)

# Frame for responses
right_frame = ctk.CTkFrame(app)
right_frame.pack(side='right', fill='both', expand=True)

# Combined input and log text box
combined_history = ctk.CTkTextbox(left_frame, state='normal', yscrollcommand=True)
combined_history.pack(fill='both', expand=True, padx=20, pady=10)
combined_history.insert(ctk.END, "You: ")  # Start the input prompt
combined_history.bind("<Return>", send_input)  # Bind the return key to send input
combined_history.bind("<Key>", lambda e: "break" if e.keysym == "Return" else None)  # Prevent new line on 'Return'

# Textbox for showing bot responses
response_history = ctk.CTkTextbox(right_frame, state='disabled', yscrollcommand=True)
response_history.pack(fill='both', expand=True, padx=20, pady=10)

app.mainloop()
