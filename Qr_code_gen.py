
from tkinter import *
import qrcode
import os

if not os.path.exists("QRcode"):
    os.makedirs("QRcode")

root = Tk()
root.title("Scans")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False, False)

def generate():
    name = title.get()
    text = entry.get()
    if name and text:
        qr = qrcode.make(text)
        qr.save("QRcode/" + name + ".png")

Label(root, text="Title", fg="white", bg="#AE2321", font=15).place(x=50, y=170)

title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=200)

entry = Entry(root, width=28, font="arial 15")
entry.place(x=50, y=250)

Button(root, text="Generate", width=20, height=2, bg="black", fg="white", command=generate).place(x=50, y=300)

root.mainloop()
