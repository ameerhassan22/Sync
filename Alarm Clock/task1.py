# Basic Libraries
import tkinter as tk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import winsound

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry('800x600')
alarms = []  # List to store alarm times
# Function to add a new alarm
def add_alarm():
    alarm_time = alarm_entry.get()
    if alarm_time:
        alarms.append(alarm_time)
        alarm_listbox.insert(tk.END, alarm_time)
        alarm_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a valid alarm time.")

# Function to remove the selected alarm
def remove_alarm():
    selected_index = alarm_listbox.curselection()
    if selected_index:
        alarms.pop(selected_index[0])
        alarm_listbox.delete(selected_index[0])
    else:
        messagebox.showwarning("Warning", "Please select an alarm to remove.")

# Function to update the clock label
def update_time():
    current_time = strftime("%H:%M:%S %p")
    time_label.config(text=current_time)
    check_alarms()
    root.after(1000, update_time)

# Function to check for triggered alarms
def check_alarms():
    current_time = datetime.now().strftime("%H:%M")
    for alarm in alarms:
        if alarm == current_time:
                messagebox.showinfo("Alarm", f"Alarm triggered at {alarm}!")
                winsound.PlaySound("alarm.wav",winsound.SND_ASYNC)
# Create and configure widgets

tk.Label(root,text="Alarm Clock",font=("Helvetica",50 ,"bold"),fg="red").pack(pady=10)

time_label = tk.Label(root, text="", font=("Helvetica", 35,"bold"))
time_label.pack(pady=20)

alarm_label = tk.Label(root, text="Set Alarm (Hours:Minutes)", font=("Helvetica", 16,"bold"),fg="green")
alarm_label.pack()

alarm_entry = tk.Entry(root, font=("Helvetica", 24),fg="yellow",background='#115e5f')
alarm_entry.pack()

add_button = tk.Button(root, text="Add Alarm", command=add_alarm, font=("Helvetica", 16,"bold"),fg="blue")
add_button.pack(pady=5)

alarm_remove = tk.Entry(root, font=("Helvetica", 24,"bold"),fg="red")
alarm_entry.pack()

remove_button = tk.Button(root, text="Remove Alarm", command=remove_alarm, font=("Helvetica", 16,"bold"),fg="Maroon")
remove_button.pack(pady=5)

alarm_listbox = tk.Listbox(root, font=("Helvetica", 16,"bold"))
alarm_listbox.pack()

# Start the time update loop
update_time()

# Run the Tkinter main loop
root.mainloop()
