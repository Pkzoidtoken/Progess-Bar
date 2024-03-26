from tkinter import *
import threading
import time

root = Tk(className="ProgessBar")

root.geometry("600x150")

root.config(
    background='black',
)

#progess bar
background_progess = Label(root,background="#3B3B3B",width=30,height=2)
background_progess.grid(column=0,row=0,padx=50,pady=50)

upper_progess = Label(root,background="#4751ED",width=0,height=2)
upper_progess.grid(column=0,row=0,padx=50,pady=50)

#count label %0
count_lab = Label(root,text="%0",font=("semibold","12"),foreground="white",bd=0,background="black")
count_lab.place(x=10,y=10)

#play button image
play_icon = PhotoImage(file="play.png")

#update progess using loop
def update_progess():
    count = 0
    for i in range(0,31):
        time.sleep(0.05)
        count += 1
        if i == 30:
            root.after(0,lambda:upper_progess.config(width=0,height=1))
            count_lab.configure(text=f"%{count}")
            background_worker()
        else:
            count_lab.configure(text=f"%{count}")
            root.after(0,lambda i=i:upper_progess.config(width=i,height=1))

#run threading background
def background_worker():
    task1 = threading.Thread(target=update_progess)
    task1.start()

#when user click on button change image
def click_on_button():
    play_icon.configure(file="click.png")
    time.sleep(0.2)
    play_icon.configure(file="play.png")
    background_worker()

#when user click on button then run background function click_on_button
def background_worker1():
    task1 = threading.Thread(target=click_on_button)
    task1.start()

#play button label
play_button = Label(root,image=play_icon,border=0,borderwidth=0,background="black")
play_button.grid(column=1,row=0,padx=50,pady=50)

#bind label play button to make clickable
play_button.bind("<Button-1>",lambda e:background_worker1())

root.mainloop()