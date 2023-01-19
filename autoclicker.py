from tkinter import *
import pyautogui
import time



root=Tk()
root.geometry("500x170")
root.title("autoclicker")

posx_label=Label(text="x position :", font=("Arial", 15, "bold")).grid(row=0, column=0)
posx_entry=Entry(root, width=18)
posx_entry.grid(row=0, column=2)

posy_label=Label(text="y position :", font=("Arial", 15, "bold")).grid(row=1, column=0)
posy_entry=Entry(root, width=18)
posy_entry.grid(row=1, column=2)

sleep_label=Label(text="sleep time :", font=("Arial", 15, "bold")).grid(row=2, column=0)
sleep_entry=Entry(root, width=18)
sleep_entry.grid(row=2, column=2)

repeat_label=Label(text="nbr clicks:", font=("Arial", 15, "bold")).grid(row=3, column=0)
repeat_entry=Entry(root, width=18)
repeat_entry.grid(row=3, column=2)

def start():
    posx=posx_entry.get()
    posy=posy_entry.get()
    if int(posx) == 0 and int(posy) == 0:
        for i in range(int(repeat_entry.get())):
            pyautogui.click()
            time.sleep(int(sleep_entry.get()))
    else:
        for i in range(int(repeat_entry.get())):
            pyautogui.click(int(posx), int(posy))
            time.sleep(int(sleep_entry.get()))

start_button=Button(root, command=start, text="start", font=("Arial", 15, "bold"), width=18)
start_button.grid(row=4, column=0)



root.mainloop()
