# IMPORTS
from tkinter import *

# VARIABLES 
FONT_NAME = "Arial"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

stage = ""
rounds = 0
seconds = 0
minutes = 0
timer = "25:00"
reset = False
select = True
start_status = False

# FUNTION
def countdown():

    global timer, start_status, status_text, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, reset, rounds, select, seconds, minutes, stage
    start_status = True

    # RESET
    if reset == True:

        stage = ""
        rounds = 0
        seconds = 0
        minutes = 0
        timer = "00:00"
        reset = False
        select = True
        start_status = False

        canvas.itemconfig(status_text, text="TIMER", fill="#393E46")
        canvas.itemconfig(timer_text, text="25:00")
        canvas.itemconfig(stage_text, text="")
        return
    
    # TIME SELECT
    if select == True:
        if rounds in [0, 2, 4, 6]:
            select = False
            minutes = WORK_MIN
            canvas.itemconfig(status_text, text="WORK", fill = "#E55050")
        elif rounds in [1, 3, 5]:
            select = False
            minutes = SHORT_BREAK_MIN
            canvas.itemconfig(status_text, text="BREAK", fill = "#5A827E")
        elif rounds == 7:
            select = False
            minutes = LONG_BREAK_MIN
            canvas.itemconfig(status_text, text="BREAK", fill = "#5A827E")
        elif rounds >= 8:
            restart()
            window.after(1000, countdown)

    # MAIN TIMER
    if seconds == 0 and minutes > 0:
        seconds = 59 
        minutes -= 1
    elif seconds > 0:
        seconds -= 1

    # BEGINNING AFTER THE END
    if minutes == 0 and seconds == 0:

        seconds = 0
        minutes = 0
        timer = f"00 : 00"
        select = True
        start_status = False

        if rounds in [0, 2, 4, 6]:
            stage += "✔"

        canvas.itemconfig(timer_text, text=timer)
        canvas.itemconfig(stage_text, text=" ".join(stage))
        rounds += 1

    # SCREEN UPDATE PER SECOND
    timer = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=timer)
    window.after(1000, countdown)


def restart():
    global reset
    reset = True


# UI SETUP 
window = Tk()
window.title("Tomodoro")

canvas = Canvas(width=700, height=700)
canvas.config(bg= "#F2F2F0")
tomato_img = PhotoImage(file="Default_A_stylized_highcontrast_black_tomato_illustration_with_2_15b9f683-fda2-42e7-9c2f-40cb3798a77e_0.png")
canvas.create_image(350, 350, image=tomato_img)

timer_text = canvas.create_text(350, 430, text=timer, font=(FONT_NAME, 60, "bold"), fill="#F2F2F0")
status_text = canvas.create_text(350, 85, text="TIMER", font=(FONT_NAME, 40, "bold"), fill="#393E46")
stage_text = canvas.create_text(340, 620, text=stage, font=(FONT_NAME, 20, "bold"), fill="#393E46")
canvas.grid()

start_button = Button(
    text="Start", 
    font=(FONT_NAME, 12, "bold"), 
    command=lambda: countdown() if start_status == False else None
)
start_button.place(x=130, y=515)

reset_button = Button(
    text="Reset", 
    font=(FONT_NAME, 12, "bold"),
    command = lambda:restart()
)
reset_button.place(x=510, y=515)

window.mainloop() 