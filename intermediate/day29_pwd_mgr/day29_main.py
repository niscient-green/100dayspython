# Niscient Password Manager

from tkinter import *
from tkinter import messagebox
import pandas as pd
import pyperclip
import password_generator as pg

# Constants, Globals  -----------------------------------------------------------------------------
# Color, font
RED = "#e7305b"
FONT_NAME = "Courier"
FONT_SIZE = 12
ITEM_PADDING = 5
DEFAULT_USERNAME = "jane@doe.com"
password_df = pd.read_csv("passwords.csv")


# Read, write to file -----------------------------------------------------------------------------
def save_password():
    # Gets password info, appends to existing passwords, writes to file
    global password_df
    website_str = website_ent.get()
    username_str = username_ent.get()
    password_str = password_ent.get()

    if website_str == "" or username_str == "" or password_str == "":
        messagebox.showinfo(title="Oops", message="Please fill in all fields")
    else:
        ok_boo = messagebox.askokcancel(title=website_str, message=f"Accept these password details?\nUsername: "
                                                                   f"{username_str}\nPassword: {password_str}")

        if ok_boo:
            new_entry_ser = pd.Series({'website': website_str, 'username': username_str, 'password': password_str})
            password_df = pd.concat([password_df, new_entry_ser.to_frame().T], ignore_index=True)
            password_df.to_csv("passwords.csv", index=False)
            reset_ui()


# UI Updates --------------------------------------------------------------------------------------
def reset_ui():
    # Reset the entry fields to empty
    website_ent.delete(0, END)
    password_ent.delete(0, END)


def generate_password():
    # Generate a new password and add it to the entry box
    new_password = pg.generate_password()
    password_ent.delete(0, END)
    password_ent.insert(0, new_password)

    # Copy it to the clipboard
    pyperclip.copy(new_password)


# UI Setup ----------------------------------------------------------------------------------------
# Create window
window = Tk()
window.title("Niscient's Password Manager")
window.config(padx=40, pady=40)

# Create logo image
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Create field labels
website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0)
username_lbl = Label(text="Email / Username:")
username_lbl.grid(row=2, column=0)
password_lbl = Label(text="Password:")
password_lbl.grid(row=3, column=0)

# Create entry fields
website_ent = Entry(width=35)
website_ent.grid(row=1, column=1, columnspan=2)
website_ent.focus()
username_ent = Entry(width=35)
username_ent.insert(END, string=DEFAULT_USERNAME)
username_ent.grid(row=2, column=1, columnspan=2)
password_ent = Entry(width=21)
password_ent.grid(row=3, column=1)

# Create buttons
genpwd_btn = Button(text="Generate Password", command=generate_password)
genpwd_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)

# Create and run window
window.mainloop()
