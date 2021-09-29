from tkinter import *
from tkinter import messagebox
import requests

gui = Tk(className=":DD")
inf = Entry(gui, borderwidth=2, relief="solid")
gui.geometry("240x75")
gui.resizable(0, 0)

label1 = Label(gui, text="  Provide cfx.re link:")
label2 = Label(gui)
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
inf.grid(row=0, column=1)

def searchip():
    try:
        if not inf.get():
            messagebox.showerror("ERROR!", "Link textbox can't be empty!")
        else:
            respo = requests.get("https://" + inf.get())
            respo.raise_for_status()
            ip = (respo.headers["X-Citizenfx-Url"])
            ipcut = ip.replace("http://", "")
            messagebox.showinfo("IP has been found!", "IP: " + ipcut.replace("/", ""))
    except requests.ConnectionError as e:
        messagebox.showerror("ERROR!", "Connection error!")


oki = Button(gui, text="Find", padx=40, command=searchip)
oki.grid(row=2, column=1)

gui.mainloop()
