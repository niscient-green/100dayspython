# Niscient Password Manager

from tkinter import *

# Constants, Globals  -----------------------------------------------
# Color, font
RED = "#e7305b"
FONT_NAME = "Courier"
FONT_SIZE = 12
ITEM_PADDING = 5

# UI Setup ----------------------------------------------------------
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
username_ent.insert(END, string="jane@doe.com")
username_ent.grid(row=2, column=1, columnspan=2)
password_ent = Entry(width=21)
password_ent.grid(row=3, column=1)

# Create buttons
genpwd_btn = Button(text="Generate Password")
genpwd_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=36)
add_btn.grid(row=4, column=1, columnspan=2)


# Create and run window
window.mainloop()
