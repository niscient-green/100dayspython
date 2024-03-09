# Convert from mi to km

from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Niscient mi to km converter")
window.config(padx=50, pady=50)

# Create labels
miles = Label(text="Miles")
miles.grid(row=0, column=2)
is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)
converted = Label(text="0")
converted.grid(row=1, column=1)
km = Label(text="Km")
km.grid(row=1, column=2)

# Create text entry box
miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(row=0, column=1)


# Create button
def convert():
    new_km = float(miles_entry.get()) * 1.60934
    converted.config(text=round(new_km, 1))


calc_button = Button(text="Calculate", command=convert)
calc_button.grid(row=2, column=1)


# Run window loop
window.mainloop()
