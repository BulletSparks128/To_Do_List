from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
import os

# Set a default file path for automatic saving
default_file = "C:\\Users\\laura\\OneDrive\\Documents\\TodoList"

root = Tk()
root.title('To-Do List!')
root.geometry("600x500")

#Define font
list_font = Font(
    family="Courier New",
    size=10,
    weight="bold"
)

#Define font
my_font = Font(
    family="Courier New",
    size=10,
    weight="bold"
)

#Create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#Create listbox
my_list = Listbox(
    my_frame,
    font=list_font,
    width=53,
    height=20,
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
my_entry = Entry(root, font=("Courier New", 14), width=40)
my_entry.pack(pady=20)

#Button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#Functions

def delete_item(event=None):
    my_list.delete(ANCHOR)  # Delete the currently selected item

def add_item(event=None):
    item = my_entry.get().strip()  # Get input and strip whitespace
    if item:  # Check if input is not empty
        my_list.insert(END, item)  # Insert item into the listbox
        my_entry.delete(0, END)  # Clear the entry box

my_entry.bind('<Return>', add_item)
my_list.bind('<BackSpace>', delete_item)

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

def save_list(auto_save=False):
    file_name = default_file if auto_save else filedialog.asksaveasfilename(
        initialdir="C:\\Users\\laura\\OneDrive\\Documents\\TodoList",
        title="Save File",
        filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )

    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        # Delete crossed off items before saving
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1

        # Grab all the items from the list
        stuff = my_list.get(0, END)

        # Open the file for saving
        with open(file_name, 'wb') as output_file:
            pickle.dump(stuff, output_file)

def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:\\Users\\laura\\OneDrive\\Documents\\TodoList",
        title="Open FIle",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*")
        )
    )

    if file_name:
        #Delete currently open list
        my_list.delete(0, END)

        #Open teh file
        input_file = open(file_name, 'rb')

        #Load the data from the file
        stuff = pickle.load(input_file)

        #Output stuff to the screen
        for item in stuff:
            my_list.insert(END, item)

def delete_list():
    my_list.delete(0, END)

#Creat Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add items to menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label= "File", menu=file_menu)

#Add dropdowns
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=delete_list)

# Main buttons
delete_button = Button(
    button_frame,
    text="Delete",
    command=delete_item,
    font=my_font
)

add_button = Button(
    button_frame,
    text="Add",
    command=add_item,  # Button still uses add_item
    font=my_font
)

cross_off_button = Button(
    button_frame,
    text="Cross Off",
    command=cross_off_item,
    font=my_font
)

uncross_button = Button(
    button_frame,
    text="Uncross",
    command=uncross_item,
    font=my_font
)

delete_crossed_button = Button(
    button_frame,
    text="Delete Crossed",
    command=delete_crossed,
    font=my_font
)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

# Main loop
root.mainloop()