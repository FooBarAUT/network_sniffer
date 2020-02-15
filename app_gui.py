from src import macadress
from src import ping
from tkinter import ttk
import tkinter


def validate_input(number):
    try:
        if(int(number) > 254):
            number = 254
        elif(int(number) < 1):
            number = 1
        else:
            pass
        return int(number)

    except Exception:
        pass


def partial():
    tbox.delete(1.0, tkinter.END)
    start = validate_input(spin1.get())
    end = validate_input(spin2.get())
    if(start and end):
        results = ping.get_confirmed_adresses(start, end)
        for ip in results:
            tbox.insert(tkinter.END, ip + "\n")
    else:
        pass


def full():
    tbox.delete(1.0, tkinter.END)
    results = ping.get_confirmed_adresses(1, 254)
    for ip in results:
        tbox.insert(tkinter.END, ip + "\n")


window = tkinter.Tk()

window.title("Welcome to FooBarAUT's app")
window.geometry("600x200")

sbar = tkinter.Scrollbar(window)
tbox = tkinter.Text(window, height=4, width=15)
sbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
tbox.pack(side=tkinter.LEFT, fill=tkinter.Y)
sbar.config(command=tbox.yview)
tbox.config(yscrollcommand=sbar.set)

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Custom IP range')
tab_control.add(tab2, text='Full IP range')

# -- begin custom IP range tab -- #
lbl1 = tkinter.Label(tab1, text="Custom IP range", font=("Arial Bold", 30))
lbl1.grid(column=0, row=0)

spin1 = tkinter.Spinbox(tab1, from_=1, to=253, width=5)
spin1.grid(column=0, row=1)
spin2 = tkinter.Spinbox(tab1, from_=2, to=254, width=5)
spin2.grid(column=1, row=1)


btn1 = tkinter.Button(tab1, text="Click Me!",
                      bg="lightgreen", fg="black", command=partial)
btn1.grid(column=2, row=1)
# -- end custom IP range tab -- #

# -- begin full IP range tab -- #
lbl2 = tkinter.Label(tab2, text="Full IP range!!", font=("Arial Bold", 35))
lbl2.grid(column=0, row=0)


btn2 = tkinter.Button(tab2, text="Click Me!",
                      bg="lightgreen", fg="black", command=full)
btn2.grid(column=1, row=1)
# -- end full IP range tab -- #

tab_control.pack(expand=1, fill='both')

window.mainloop()
