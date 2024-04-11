from tkinter import *
import requests

def get_quote():
    quote_rsp = requests.get(url="https://api.kanye.rest/")
    quote_rsp.raise_for_status()
    quote_jsn = quote_rsp.json()
    quote_str = quote_jsn["quote"]
    canvas.itemconfig(quote_text, text=quote_str)


# Set up UI
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="PLACEHOLDER", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start main loop
window.mainloop()
