import tkinter as tk
import pyshorteners as short

# Function to shorten the URL
def shorten_url():
    # Get the long URL from the entry widget
    long_url = link_entry.get()

    # Shorten the URL using the TinyURL service
    S = short.Shortener()
    short_url = S.tinyurl.short(long_url)

    # Display the shortened URL in a label
    result_label.config(text="Output:\n"+short_url)

# Create a Tkinter window
root = tk.Tk()
root.title("URL Shortener")
root.geometry('600x400')


# Create an Entry widget for user input
tk.Label(root,text="Short link",font=("Helvetica",50 ,"bold"),fg="blue").pack()


link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=10)

# Create a Button widget to shorten the URL
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url,font=("Helvetica",15 ,"bold"),fg="red")
shorten_button.pack()

# Create a Label widget to display the result
result_label = tk.Message(root, text="",font=("Helvetica",10 ,"bold"),fg="maroon")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
