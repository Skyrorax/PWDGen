import sys
import tkinter as tk
from tkinter import messagebox as mb
import generator as gen

history = []
first_screen = []
history_screen = []

font = "Arial 13 bold"


def clipboard(event):
    root.clipboard_clear()
    root.clipboard_append(event.widget["text"])


def pw_check():
    "checks wether a password is strong or not and changes background color, as well as displaying a weeak/strong/medium strength string"
    pass


def kill(*args):
    sys.exit(0)


def hide_history():
    h1.pack_forget()
    scrollbar.pack_forget()
    liste.pack_forget()


def display_history(*args):

    def listbox_click(event):

        selection = event.widget.curselection()
        value = event.widget.get(int(selection[0]))
        root.clipboard_clear()
        root.clipboard_append(value[3:])

    global h1
    h1 = tk.Button(root, text="Back", padx=root_width, bd=0, command=hide_history, font="Arial 12 bold", bg="dark grey")
    h1.pack()

    global scrollbar
    scrollbar = tk.Scrollbar(root, orient="horizontal")
    scrollbar.pack(side="bottom", fill="x")

    global liste
    liste = tk.Listbox(width=38, height=23, selectmode="SINGLE", font="Arial 11",
                       xscrollcommand=scrollbar.set, bg="dark grey", cursor="hand2")
    liste.bind("<<ListboxSelect>>", listbox_click)

    for i in range(len(history)):
        liste.insert("end", f"{i + 1}) {history[i]}")
    liste.pack()

    scrollbar.config(command=liste.xview)


def display_password(*args):  # *args needs to be here, so hitting return with empty field doesn't cause exception
    try:
        if int(digits.get()) in range(1, 201):  # WIP maybe find a better way?
            temp = gen.create_pw(int(digits.get()), get(small), get(big), get(numbers), get(symbols), get(ambiguous))
            history.append(temp)

            global label2
            if "label2" in globals():
                label2.destroy()
            label2 = tk.Label(root, font="Arial 14", bg="dark grey", justify="left", text=temp, wraplength=295,
                              cursor="hand2")
            label2.place(x=5, y=0.01 * root_height)
            label2.bind("<Button-1>", clipboard)

            global counter
            if "counter" in globals():
                counter.destroy()
            counter = tk.Label(root, font="Arial 11", bg="dark grey", justify="left", text=len(history))
            counter.place(x=25 * root_width / 40, y=0.5 * root_height)

            first_screen.extend([temp, label2, counter])

        else:
            mb.showerror(title="Error", message="Please only fill in a number between 1 and 200")
    except ValueError:
        mb.showerror(title="Error", message="Please only fill in a number between 1 and 200")


def get(tkvar):
    return tk.BooleanVar.get(tkvar)


def create_variables():
    global digits
    digits = tk.StringVar()
    global small
    small = tk.BooleanVar(value=True)
    global big
    big = tk.BooleanVar(value=True)
    global numbers
    numbers = tk.BooleanVar(value=True)
    global symbols
    symbols = tk.BooleanVar(value=True)
    global ambiguous
    ambiguous = tk.BooleanVar(value=True)


def create_widgets():
    global font

    form = tk.Entry(root, textvariable=digits, font="Arial 11", bg='white', exportselection=0, width=3)
    form.place(x=root_width / 13, y=0.55 * root_height)
    form.focus_set()

    label1 = tk.Label(root, text="Digits", font=font, bg='dark grey')
    label1.place(x=root_width / 5, y=0.55 * root_height)

    b1 = tk.Button(root, text="Generate Password", font=font, bg="green", command=display_password, fg="white",
                   cursor="hand2")
    b1.place(x=root_width / 40, y=0.45 * root_height, anchor="w")

    b2 = tk.Button(root, text="History", font=font, bg="blue", fg="white", command=display_history,
                   padx=0.08 * root_width, cursor="hand2")
    b2.place(x=39 * root_width / 40, y=0.45 * root_height, anchor="e")

    c1 = tk.Checkbutton(root, text="Small Letters", font=font, bg='dark grey', variable=small, cursor="hand2")
    c1.place(x=root_width / 15, y=9 * root_height / 14)

    c2 = tk.Checkbutton(root, text="Big Letters", font=font, bg='dark grey', variable=big, cursor="hand2")
    c2.place(x=root_width / 15, y=10 * root_height / 14)

    c3 = tk.Checkbutton(root, text="Numbers", font=font, bg='dark grey', variable=numbers, cursor="hand2")
    c3.place(x=root_width / 15, y=11 * root_height / 14)

    c4 = tk.Checkbutton(root, text="Symbols", font=font, bg='dark grey', variable=symbols, cursor="hand2")
    c4.place(x=root_width / 15, y=12 * root_height / 14)

    c5 = tk.Checkbutton(root, text="Avoid ambiguous characters", font=font, bg='dark grey', variable=ambiguous,
                        cursor="hand2")
    c5.place(x=root_width / 15, y=13 * root_height / 14)

    for widget in locals():
        first_screen.append(widget)


class Application(tk.Frame):
    def __init__(self):
        super().__init__(root)
        create_variables()
        create_widgets()


#
# ---------------------------------------------- MAIN
#

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Generator")
    root.configure(bg='dark grey')
    root.iconbitmap('flash.ico')
    root.bind('<Return>', display_password)
    root.bind('<Escape>', kill)
    root.bind('h', display_history)
    root.bind('b', hide_history)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root_width = int(0.15 * screen_width)
    root_height = int(0.4 * screen_height)

    root.geometry(f"{root_width}x{root_height}+{int(0.4 * screen_width)}+{int(0.4 * screen_height)}")
    root.resizable(False, False)
    # root.attributes("-toolwindow", 1)  # removes minimize/maximize
    app = Application()

    app.mainloop()

# TODO implement Visual Feedback on copy, -> replace copied item with "Copied!" for 1 sec and flash background light green