import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# Color, font
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Timing
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# # Debug version
# WORK_SEC = 5
# SHORT_BREAK_SEC = 5
# LONG_BREAK_SEC = 5
# Production version
WORK_SEC = WORK_MIN * 60
SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
LONG_BREAK_SEC = LONG_BREAK_MIN * 60

# Tracks all time segments (work, breaks)
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    timer_lbl.config(text="Timer", fg=GREEN)
    reps = 0
    update_checkmark()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # 1, 3, 5, 7 = Work
    # 2, 4, 6 = Short Break
    # 8 = Long Break
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown_timer(LONG_BREAK_SEC)
        timer_lbl.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown_timer(SHORT_BREAK_SEC)
        timer_lbl.config(text="Break", fg=PINK)
    else:
        countdown_timer(WORK_SEC)
        timer_lbl.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_timer(count_int):
    count_min_int = math.floor(count_int / 60)
    count_sec_int = count_int % 60

    canvas.itemconfig(timer_txt, text=f"{count_min_int:02d}:{count_sec_int:02d}")
    if count_int > 0:
        global timer
        timer = window.after(1000, countdown_timer, count_int - 1)
    else:
        update_checkmark()
        start_timer()


# Add a checkmark
def update_checkmark():
    global reps
    checkmark_count = math.ceil(reps / 2)
    checkmark_str = ""
    for check in range(0, checkmark_count):
        checkmark_str += "✔"
    checkmark_lbl.config(text=checkmark_str)


# ---------------------------- UI SETUP ------------------------------- #
# Create window
window = Tk()
window.title("Niscient's Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Create labels
timer_lbl = Label(text="Pomodoro", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_lbl.grid(row=0, column=1)
checkmark_lbl = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_lbl.grid(row=3, column=1)

# Create buttons
start_btn = Button(text="Start", command=start_timer)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(row=2, column=2)


window.mainloop()
