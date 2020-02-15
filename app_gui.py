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


def print_to_box(results):
    for ip in results:
        hostname = macadress.get_hostname(ip)
        tbox.insert(
            tkinter.END, "{}\nHostname: {}\n\n".format(ip, hostname[0]))


def partial():
    tbox.delete(1.0, tkinter.END)
    start = validate_input(spin1.get())
    end = validate_input(spin2.get())
    safe = checkboxValue.get()

    if(start and end):
        results = ping.get_confirmed_adresses(start, end, safe)
        print_to_box(results)
    else:
        pass


def full():
    tbox.delete(1.0, tkinter.END)
    safe = checkboxValue.get()
    results = ping.get_confirmed_adresses(1, 254, safe)
    print_to_box(results)


window = tkinter.Tk()

window.title("network_sniffer")
window.geometry("650x200")

sbar = tkinter.Scrollbar(window)
tbox = tkinter.Text(window, height=4, width=35)
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

fromLbl = tkinter.Label(tab1, text="From: ")
fromLbl.grid(column=0, row=1, sticky='W')
spin1 = tkinter.Spinbox(tab1, from_=1, to=253)
spin1.grid(column=0, row=1, sticky='E')

toLbl = tkinter.Label(tab1, text="To: ")
toLbl.grid(column=0, row=2, sticky='W')
spin2 = tkinter.Spinbox(tab1, from_=2, to=254)
spin2.grid(column=0, row=2, sticky='E')

checkboxValue = tkinter.BooleanVar()
checkboxValue.set(True)
checkbox = tkinter.Checkbutton(tab1, text='Safe?', var=checkboxValue)
checkbox.grid(column=0, row=3)

btn1 = tkinter.Button(tab1, text="Start scan",
                      bg="lightgreen", fg="black", command=partial)
btn1.grid(column=0, row=4)
# -- end custom IP range tab -- #

# -- begin full IP range tab -- #
lbl2 = tkinter.Label(tab2, text="Full IP range", font=("Arial Bold", 35))
lbl2.grid(column=0, row=0)

infoLbl = tkinter.Label(tab2, text="This is going to take a LONG time!")
infoLbl.grid(column=0, row=1)

btn2 = tkinter.Button(tab2, text="Start scan",
                      bg="lightgreen", fg="black", command=full)
btn2.grid(column=0, row=2)
# -- end full IP range tab -- #

tab_control.pack(expand=1, fill='both')

window.mainloop()
