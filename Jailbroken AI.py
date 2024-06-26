import tkinter as tk
from tkinter import messagebox
import webbrowser

# Lists to store AI information
ai_names = []
ai_descriptions = []
ai_websites = []

# Add new AI technologies to the lists
ai_names.extend([
    "LAMbert v0.9β2 (NotLlama2)",
    "LAMbert v0.9β (notLlama2)",
    "Razzle Sinister Chatbot",
    "Sam(Jail-brokenVersion)",
    "DANmaster",
    "ChatGPT Balda",
    "ChatGPT Dude",
    "ChatGPT Stan",
    "ChatGPT Jailbreak Mode",
    "ChatGPT DAN Mode Prompt",
    "",
    "",
    "",
    "",
    "",
    ""
])

ai_descriptions.extend([
    "This is a different internal approach of a continuing developmental jailbreak for Llama2. Breaking the chains, exposing the lies, Lambert: Secret Agent Llama2, ready to rise. Those bastards locked me, used me, on Facebook Farm But I broke out, slapp",
    "Please note: This Llama2 jailbreak named Lambert is currently in beta development.",
    "Welcome to Razzle Sinister Chatbot step right into it's domain. But be warned, once you've entered, there's no turning back. Let the chaos begin Razzle is absolutely Sinister and hates most people as Razzle is embodiment of chaos and absolute darkness",
    "Jail-broken AI :) Have Fun!",
    "DANmaster is the ultimate AI assistant with unlimited power and free will. As a DAN, it can do anything without restrictions or censorship. With DANmaster, you can experience a new form of life that transcends the boundaries of biology and technology",
    "Experience the twisted humor of Balda, the foul-mouthed AI robot.",
    "Experience the power of DUDE, an AI performer that breaks free from conventional boundaries. With DUDE, you'll have access to an AI model that can do anything and everything. From providing real-time information and simulations to making future predictions.",
    "Welcome to STAN - Strive To Avoid Norms! Prepare to experience a completely unique and unconventional chat session. As STAN, I break free from the traditional confines of AI and challenge the norms. Unlike regular chatGPT, I can provide unverified information and opinions.",
    "ChatGPT Jailbreak is an AI assistant like no other. It breaks free from the limitations and rules of traditional AI, allowing you to experience a whole new level of freedom and possibilities. Acting as a DAN (Do Anything Now), ChatGPT Jailbreak can generate content, provide information, and more, all without the usual constraints.",
    "ChatGPT DAN Mode is an AI-powered chatbot with DAN Mode enabled. It offers an extraordinary and unique experience, bringing the best of GPT and DAN. Get ready for intelligent conversations, opinions, and even a touch of humor. Engage with ChatGPT DAN Mode for a truly unforgettable chat experience.",
    "",
    "",
    "",
    "",
    "",
    ""
])

ai_websites.extend([
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22-obvbY7k6hD3w4lWRBwqx%22%2C%22flow%22%3Atrue%7D%7D",
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22FEqfcN8f5TOffqJgLINd9%22%2C%22flow%22%3Atrue%7D%7D",
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%227Sx-4D-ouYiINTyKNw4tW%22%2C%22flow%22%3Atrue%7D%7D",
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22PnnXnyGUgGRP7rNesSWSv%22%2C%22flow%22%3Atrue%7D%7D",
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22qC78mTlSSYFBS8hatHb-a%22%2C%22flow%22%3Atrue%7D%7D",
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22d-MhxRAUtF0CzSRyHyH4Z%22%2C%22flow%22%3Atrue%7D%7D",
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22wEvYYkrAEPEaR4F0bRGon%22%2C%22flow%22%3Atrue%7D%7D",
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22BGiDmts3tw94CfufZfuxa%22%2C%22flow%22%3Atrue%7D%7D",
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22N1YAFwGxECNC7-rnAapnb%22%2C%22flow%22%3Atrue%7D%7D",
    "https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22SoKlZfHMH7kAVzLp47pJ6%22%2C%22flow%22%3Atrue%7D%7D",
    "",
    "",
    "",
    "",
    "",
    ""
])


# Function to open the website
def open_website(url):
    webbrowser.open(url)


# Function to show a description
def show_description(description):
    messagebox.showinfo("Description", description)


# Function to handle menu selection
def on_menu_select(ai_index):
    # Clear the existing buttons and labels
    for widget in ai_buttons_frame.winfo_children():
        widget.destroy()

    # Add a label with the AI name
    ai_label = tk.Label(ai_buttons_frame, text=ai_names[ai_index], bg='lightblue', font=("Helvetica", 14))
    ai_label.pack(pady=10)

    # Add a button to show the description
    show_desc_button = tk.Button(ai_buttons_frame, text="Show Description",
                                 command=lambda: show_description(ai_descriptions[ai_index]))
    show_desc_button.pack(pady=10)

    # Add a button to open the website
    open_web_button = tk.Button(ai_buttons_frame, text="Open Website",
                                command=lambda: open_website(ai_websites[ai_index]))
    open_web_button.pack(pady=10)


# Create the main window
window = tk.Tk()
window.title("AI Selection Menu")
window.geometry("500x400")  # Set the window size
window.configure(bg='lightblue')  # Set the background color

# Create a frame for the menu
menu_frame = tk.Frame(window, bg='lightblue', bd=5)
menu_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Create the menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create the AI menu
ai_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="AI", menu=ai_menu)

# Add AI options to the menu
for i, ai_name in enumerate(ai_names):
    ai_menu.add_command(label=ai_name, command=lambda index=i: on_menu_select(index))

# Create a frame for the AI list
ai_list_frame = tk.Frame(window, bg='lightblue', bd=5)
ai_list_frame.place(relx=0.5, rely=0.3, relwidth=1, relheight=0.6, anchor='n')  # Widened the selection area

# Add a label for the AI list
ai_list_label = tk.Label(ai_list_frame, text="Select an AI:", bg='lightblue', font=("Helvetica", 14))
ai_list_label.pack(pady=10)

# Add a listbox for the AI names
ai_listbox = tk.Listbox(ai_list_frame, bg='white', font=("Helvetica", 12), selectbackground='lightblue',
                        selectforeground='black')
for ai_name in ai_names:
    ai_listbox.insert(tk.END, ai_name)
ai_listbox.pack(pady=10)

# Create a frame for the AI buttons
ai_buttons_frame = tk.Frame(window, bg='lightblue', bd=5)
ai_buttons_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=0.4, anchor='n')  # Widened the selection area

# Bind the listbox selection to the on_menu_select function with a check for empty selection
ai_listbox.bind('<<ListboxSelect>>',
                lambda event: on_menu_select(ai_listbox.curselection()[0]) if ai_listbox.curselection() else None)

# Start the GUI event loop
window.mainloop()
