# Basic Libraries
import tkinter as tk

# tkinker basic
window = tk.Tk()
window.title("Chatbot")
window.geometry('600x800')
window.config(background='#024497')

# methods
rules = [
    ("Hello", "\nHi"),
    ("How are you?", "\nI'm just a tour guide chatbot, I have no feelings"),
    ("What's your name?", "\nI'm a chatbot."),
    ("What is AI?", "\nAI stands for Artificial Intelligence.\nIt refers to the simulation of human intelligence in machines."),
    ("What are the applications of AI?", "\nAI has various applications, such as natural language processing, computer vision, robotics, and data analysis."),
    ("How does AI impact our daily lives?", "\nAI has a significant impact on our daily lives,\nfrom voice assistants like Siri and Alexa to personalized recommendations on streaming platforms."),
    ("What are some examples of AI in use today?", "\nSome examples of AI in use today include self-driving cars,\nvirtual personal assistants, and fraud detection systems."),
    ("what is type of machine learning algorithms?","\n1.Self-supervised learning\n\n2.Unsupervised Learning\n\n3.Reinforcement Learning\n\n4.Self-Supervised Learning\n\n5.Semi-Supervised Learning\n\n6.Deep Learning"),
    ("what is language of computer?","\nBinary Numbers(ASCII Code)"),
    ("how can represent clours?","\n1.RGB\t2.Hexadecimal\t\t3.HSL")  ]

def get_response():
    user_input = entry.get()
    display_text = f"You:\n{user_input}"
    chat_text.insert(tk.END, display_text)
    entry.delete(0, tk.END)
    
    for question, response in rules:
        if user_input.lower() in question.lower():
            chat_text.insert(tk.END, f"\n\nChatbot: {response}\n\n")
            return    
    chat_text.insert(tk.END, "Chatbot: I'm sorry, I don't have a specific response to that question.\n\n")

#labels
heading = tk.Label(window,text='Chatbot',font=('Helvetica',40,'bold'),background='#024497',fg='white')
heading.place(x=50,y=50)

# chatpot label to anwer
chat_text = tk.Text(window, width=70, height=20,font=('Helvetica',15,'bold'),background='white',fg='black')
chat_text.place(x=570,y=100)

entry_label = tk.Label(window, text="You",font=('Helvetica',30,'bold'),background='#024497',fg='white')
entry_label.place(x=50,y=200)

entry = tk.Entry(window, width=70,font=('Helvetica',10,'bold'),background='white',fg='black')
entry.place(x=50,y=250)

submit_button = tk.Button(window, text="Submit",font=('Helvetica',20,'bold'),background='yellow', command=get_response)
submit_button.place(x=50,y=300)

# run tkinker
window.mainloop()