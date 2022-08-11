from tkinter import *
import random as ran, datetime as dt
from tkinter import messagebox






# ********************************************************** CONSTANTS *********************************************************

p_choice = None
c_choice = None
score_win = 0
score_lose = 0
score_draw = 0











# ********************************************************** FUNCTIONS *********************************************************






def page1():
    global fpage
    fpage = Toplevel(app)
    fpage.title("Rock Paper Scissors")
    fpage.iconbitmap("./Assets/RPS_logo.ico")
    fpage.config(padx=50, pady=60)

    screen_width = fpage.winfo_screenwidth()
    screen_height = fpage.winfo_screenheight()
    window_height = 750
    window_width = 883
    width_center = int(screen_width/2 - window_width/2)
    height_center = int(screen_height/2 - window_height/2)
    window_position = fpage.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
    fpage.resizable(False, False)
    
    canvas = Canvas(
        fpage,
        width=792,
        height=532,
    )
    canvas.create_image(
        396,286,
        image = photo
    )
    canvas.grid(row=0, column=0)
    
    global name
    name = Entry(
        fpage,
        width=30,
        font=("courier", 24, "bold"),
        bg="black",
        fg="white",
        border=0,
    )
    name.focus()
    name.grid(row=2, column=0)
    
    namelabel = Label(
        fpage,
        text="Player Name",
        font=("courier", 24, "bold"),
    )
    namelabel.grid(row=1, column=0)
    
    continuebtn = Button(
        fpage,
        text="Continue",
        pady=5,
        command=record
    )
    continuebtn.grid(row=3, column=0)
    
    fpage.bind('<Return>', lambda event: record())
    
    signature = Label(
        fpage,
        text="© App by: Boateng Jephthah Agyenim", 
        font=("Signatura",14),
        pady=20
    )
    signature.grid(row=4, column=0)




def win():
    global output
    output = Toplevel(app)
    output.config(
        padx=50,
        pady=50
    )
    output.title("Rock Paper Scissors")
    output.iconbitmap("./Assets/RPS_logo.ico")
    output.config(padx=50, pady=60)

    screen_width = output.winfo_screenwidth()
    screen_height = output.winfo_screenheight()
    window_height = 450
    window_width = 400
    width_center = int(screen_width/2 - window_width/2)
    height_center = int(screen_height/2 - window_height/2)
    window_position = output.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
    output.resizable(False, False)
    
    label = Label(
        output,
        image=p_win,
        pady=10
    )
    label.grid(row=0, column=0)
    
    again = Button(
        output,
        text="AGAIN",
        font=("courier", 24, "bold"),
        padx=10,
        pady=10,
        command=dest
    )
    again.grid(row=1, column=0)
    
    global score_win
    score_win += 1
    
    if score_win < 10:
        wins.configure(
            text = f"Wins: 0{score_win}"
        )
    else:
        wins.configure(
            text = f"Wins: {score_win}"
        )
        
        
    now = dt.datetime.now()
    date = now.date()
    time = now.time()
    
    with open("Results.txt", "a") as file:
        file.write(
            f"\n        {p_choice}        |        {c_choice}        |        {date} ({time})        |        Won"
        )
                
    output.bind('<Return>', lambda event: dest())

    
    
    
    
def dest():
    canvas1.itemconfig(p_image, image="")
    canvas2.itemconfig(com_image, image="")
    output.destroy()
    
    
    

def lose():
    global output
    output = Toplevel(app)
    output.config(
        padx=50,
        pady=50
    )
    output.title("Rock Paper Scissors")
    output.iconbitmap("./Assets/RPS_logo.ico")
    output.config(padx=50, pady=60)

    screen_width = output.winfo_screenwidth()
    screen_height = output.winfo_screenheight()
    window_height = 450
    window_width = 430
    width_center = int(screen_width/2 - window_width/2)
    height_center = int(screen_height/2 - window_height/2)
    window_position = output.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
    output.resizable(False, False)
    
    label = Label(
        output,
        image=p_lose,
        pady=10
    )
    label.grid(row=0, column=0)
    
    again = Button(
        output,
        text="AGAIN",
        font=("courier", 24, "bold"),
        padx=10,
        pady=10,
        command=dest
    )
    again.grid(row=1, column=0)
    
    global score_lose
    score_lose += 1
    
    if score_lose < 10:
        losses.configure(
            text = f"Losses: 0{score_lose}"
        )
    else:
        losses.configure(
            text = f"Losses: {score_lose}"
        )
        
    now = dt.datetime.now()
    date = now.date()
    time = now.time()
    
    with open("Results.txt", "a") as file:
        file.write(
            f"\n        {p_choice}        |        {c_choice}        |        {date} ({time})        |        Lost"
        )

        
    output.bind('<Return>', lambda event: dest())

     



def draw():
    global output
    output = Toplevel(app)
    output.config(
        padx=50,
        pady=50
    )
    output.title("Rock Paper Scissors")
    output.iconbitmap("./Assets/RPS_logo.ico")
    output.config(padx=50, pady=60)

    screen_width = output.winfo_screenwidth()
    screen_height = output.winfo_screenheight()
    window_height = 460
    window_width = 500
    width_center = int(screen_width/2 - window_width/2)
    height_center = int(screen_height/2 - window_height/2)
    window_position = output.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
    output.resizable(False, False)
    
    label = Label(
        output,
        image=p_draw,
        pady=10
    )
    label.grid(row=0, column=0)
    
    again = Button(
        output,
        text="AGAIN",
        font=("courier", 24, "bold"),
        padx=10,
        pady=10,
        command=dest
    )
    again.grid(row=1, column=0)
    
    global score_draw
    score_draw += 1
    
    if score_draw < 10:
        draws.configure(
            text = f"Draws: 0{score_draw}"
        )
    else:
        draws.configure(
            text = f"Draws: {score_draw}"
        )
        
    now = dt.datetime.now()
    date = now.date()
    time = now.time()
    
    with open("Results.txt", "a") as file:
        file.write(
            f"\n        {p_choice}        |        {c_choice}        |        {date} ({time})        |        Drawed"
        )
        
    output.bind('<Return>', lambda event: dest())

    
    


def record():
    
    if len(name.get()) < 1:
        messagebox.showwarning(
            "Player Name",
            message="Fill in the Player Name!" 
        )
    else:
        p_name = name.get()
        with open("Results.txt", "a") as file:
            file.write(
                f"\n{p_name} --:  "     
            )    
        fpage.destroy()




def choiceRock():
    global p_choice
    p_choice = "Rock    "
    canvas1.itemconfig(p_image, image=prock)
        
    check()

    if c_choice == "c_rock    ":
        draw()
    elif c_choice == "c_paper   ":
        lose()
    elif c_choice == "c_scissors":
        win()
    



def choicePaper():
    global p_choice
    p_choice = "Paper   "
    canvas1.itemconfig(p_image, image=ppaper)

    check()    
    
    if c_choice == "c_rock    ":
        win()
    elif c_choice == "c_paper   ":
        draw()
    elif c_choice == "c_scissors":
        lose()




def choiceScissors():
    global p_choice
    p_choice = "Scissors"
    canvas1.itemconfig(p_image, image=pscissors)

    check()
    
    if c_choice == "c_rock    ":
        lose()
    elif c_choice == "c_paper   ":
        win()
    elif c_choice == "c_scissors":
        draw()


def check():
    
    global c_choice
    c_choice = ran.choice(["c_rock    ", "c_paper   ", "c_scissors"])
    
    if c_choice == "c_rock    ":
        canvas2.itemconfig(com_image, image=comrock)
    elif c_choice == "c_paper   ":
        canvas2.itemconfig(com_image, image=compaper)
    else:
        canvas2.itemconfig(com_image, image=comscissors)






# ********************************************************** GUI ***********************************************************






app = Tk()
app.title("Rock Paper Scissors")
app.iconbitmap("./Assets/RPS_logo.ico")
app.config(padx=50, pady=60)


screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_height = 750
window_width = 883
width_center = int(screen_width/2 - window_width/2)
height_center = int(screen_height/2 - window_height/2)
window_position = app.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
app.resizable(False, False)

# adding images
p_win = PhotoImage(file="./Assets/won.png")
p_lose = PhotoImage(file="./Assets/lost.png")
p_draw = PhotoImage(file="./Assets/draw.png")
prock = PhotoImage(file="./Assets/player_rock.png")
ppaper = PhotoImage(file="./Assets/player_paper.png")
pscissors = PhotoImage(file="./Assets/player_scissors.png")
comrock = PhotoImage(file="./Assets/com_rock.png")
compaper = PhotoImage(file="./Assets/com_paper.png")
comscissors = PhotoImage(file="./Assets/com_scissors.png")
photo = PhotoImage(file="./Assets/RPS_logo.png")



wins = Label(
    text="Wins: 00",
    font=("courier", 30, "bold"),
    fg="green"
)
wins.grid(row=0, column=0)

draws = Label(
    text="Draws: 00",
    font=("courier", 30, "bold"),
    fg="blue"
)
draws.grid(row=0, column=1)

losses = Label(
    text="Losses: 00",
    font=("courier", 30, "bold"),
    fg="red"
)
losses.grid(row=0, column=2)

plabel = Label(
    text="PLAYER:",
    font=("courier", 50, "bold"),
    pady=20
)
plabel.grid(row=1, column=0)


comlabel = Label(
    text="COMPUTER:",
    font=("courier", 50, "bold"),
    pady=20
)
comlabel.grid(row=1, column=2)


canvas1 = Canvas(
    width=220,
    height=300,
    highlightthickness= 0
)
p_image = canvas1.create_image(
    110,150,
    image = "",
)
canvas1.grid(row=2, column=0)


vs_label = Label(
    text="VS",
    font=("courier", 80, "bold"),
    padx=100,
    pady=100
)
vs_label.grid(row=2, column=1)

canvas2 = Canvas(
    width=220,
    height=220,
    highlightthickness= 0
)
com_image = canvas2.create_image(
    110,110,
    image = ""
)
canvas2.grid(row=2, column=2)


# creating the RPS buttons
rbutton = Button(
    text="Rock", 
    font=("Arial Black", "26", "bold"),
    padx=20,
    pady=20,
    command=choiceRock
)
rbutton.grid(row=3, column=0)

pbutton = Button(
    text="Paper",
    font=("Arial Black", "26", "bold"),
    padx=20,
    pady=20,
    command=choicePaper
)
pbutton.grid(row=4, column=1)

sbutton = Button(
    text="Scissors", 
    font=("Arial Black", "26", "bold"),
    padx=20,
    pady=20,
    command=choiceScissors
)
sbutton.grid(row=3, column=2)

signature = Label(
    text="© App by: Boateng Jephthah Agyenim", 
    font=("Signatura",14),
    pady=50
)
signature.grid(row=5, column=1)




# key bindings

app.bind('<R>', lambda event: choiceRock())
app.bind('<r>', lambda event: choiceRock())
app.bind('<s>', lambda event: choiceScissors())
app.bind('<S>', lambda event: choiceScissors())
app.bind('<p>', lambda event: choicePaper())
app.bind('<P>', lambda event: choicePaper())







page1()



app.mainloop()
