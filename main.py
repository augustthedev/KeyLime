import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
window.iconbitmap(r"C:\\Users\\offic\\Downloads\\keyLimelogo.ico")


def change_color():
    color = colorchooser.askcolor(title="pick a color... NOW")
    text_area.config(fg=color[1])


def new_file():
    window.title("untitled")
    text_area.delete(1.0, END)
def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                                    defaultextension=".txt",
                                                    filetypes=[("All Files", "*.*"),
                                                                ("Text Documents", "*.*")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        finally:
            file.close


def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())

    finally:
     file.close()








def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("welcome to keylime", "keylime is a python built text editor!")

def quit():
    window.destroy()

window = Tk()
window.title("KeyLime")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x , y))

font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("10")

text_area = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=2, column=10)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="file", menu=file_menu)

file_menu.add_command(label="new", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="edit" , menu=edit_menu)
edit_menu.add_command(label="cut", command=cut)
edit_menu.add_separator()
edit_menu.add_command(label="copy", command=copy)
edit_menu.add_separator()
edit_menu.add_command(label="paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="help" , menu=help_menu)
help_menu.add_command(label="about", command=about)




















scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)



window.mainloop()