import random
import smtplib
import tkinter as tk
from tkinter import *

# Create tkinter 
otp= Tk()
otp.geometry('800x600')
otp.config(background='#0d295c')

# method
def generateOTP():
    randomCode = ''.join(str(random.randint(0, 9)) for i in range(6))
    return randomCode


sender = 'leilahamada89@gmail.com'
password = 'fvypeunocpzhllkz'
code = generateOTP()


def connectingSender():
    receiver = receiverMail.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    sendingMail(receiver, server)


def sendingMail(receiver, server):
    msg = 'Hello! \n This is your OTP is ' + code
    server.sendmail(sender, receiver, msg)
    server.quit()


def checkOTP():
    if code == codeEntry.get():
        accept = Label(otp, text='Successful Verification!', background='#0d295c',fg='green', font=('Helvetica', 20))
        accept.place(x=230, y=350)
    else:
        refuse = Label(otp, text='Unsuccessful Verification!', fg='yellow',background='#0d295c', font=('Helvetica', 20))
        refuse.place(x=230, y=350)

# labels
OTP = tk.Label(text='OTP Verification',fg='yellow',background='#0d295c',font=('Helvetica',40))
OTP.pack()

mailMsg = Label(otp, text="Email",bg='#0d295c',fg='white', font=("Helvetica", 20))
mailMsg.pack()

receiverMail = Entry(otp, text='mail.gmail.com', width=35, font=("Helvetica", 20),background='white',fg='black')
receiverMail.pack()
receiverM = StringVar()

sendOTP = Button(otp, text="send OTP", width=8, height=1, font=("Helvetica", 20),background="#f3c45d", fg="#143b03", command=connectingSender)
sendOTP.pack()

otpMsg = Label(otp, text="OTP", background='#0d295c', fg='white',font=('Helvetica', 20))
otpMsg.pack()

codeEntry = Entry(otp,font=("Helvetica", 20))
codeEntry.pack()

verify = Button(otp, text="Verify", width=8, height=1, font=("Helvetica", 20), background="#f3c45d", fg="#143b03",
                command=checkOTP)
verify.pack()

otp.mainloop()