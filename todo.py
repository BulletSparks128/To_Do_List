from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('To-Do List!')
root.geometry("500x500")

#Define font
my_font = Font(
    family="Brush Script MT",
    size=30,
    weight="bold"
)

#Create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#Create listbox
my_list = Listbox(
    my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"
)

my_list.pack(
    side=LEFT,
    fill=BOTH
)

#Dummy list
stuff = ["Fazer a capa", "Fazer contra-capa", "Escrever agradecimentos", "Escrever epígrafe"]

#Add dummy list to listbox
for item in stuff:
    my_list.insert(END, item)

#Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(
    side=RIGHT,
    fill=BOTH
)

#Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#Entry box
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

#Button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#Functions
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede"
    )

    my_list.selection_clear(0, END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646"
    )

    my_list.selection_clear(0, END)

def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))

        count += 1

#Buttons
delete_button = Button(
    button_frame,
    text="Delete",
    command=delete_item
)

add_button = Button(
    button_frame,
    text="Add",
    command=add_item
)

cross_off_button = Button(
    button_frame,
    text="Cross Off",
    command=cross_off_item
)

uncross_button = Button(
    button_frame,
    text="Uncross",
    command=uncross_item
)

delete_crossed_button = Button(
    button_frame,
    text="Delete Crossed",
    command=delete_crossed
)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()