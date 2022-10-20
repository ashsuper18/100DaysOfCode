from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_time_label, text="00:00")
    timer_text.config(text="Pomodoro", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_text.config(text="Enjoy Break !!", fg=RED)
        window.bell()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_text.config(text="Break", fg=PINK)
        window.bell()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)

    else:
        countdown(work_sec)
        timer_text.config(text="Work", fg=GREEN)
        window.bell()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_time_label, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        # for check marks
        marks = ""
        works_session = math.floor(reps/2)
        for _ in range(works_session):
            marks = "✔️"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# to add image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"028_Day28_Pomodoro\tomato2.gif")
canvas.create_image(100, 112, image=tomato_img)

# to add timer in center
timer_time_label = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


#  timer label
timer_text = Label(text="POMODORO", fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)

timer_text.grid(row=1, column=2)


# start and reset button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=3)


# tick label
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=4, column=2)


# -----------------------EXTRA ---------------------------------#
# NOTES trying to bring the window forward when timer start
# window.lift()
# window.attributes('-topmost', True)
# window.attributes('-topmost', False)

window.mainloop()
