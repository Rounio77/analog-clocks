import tkinter as tk
import time
import math

window = tk.Tk()
window.geometry("400x400")
def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))
    
    # Updating seconds time
    second_x = second_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    second_y = -1 * second_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(second_hand, center_x, center_y, second_x, second_y)    
    
    # Updating hours time
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)
    
    # Updating minutes time
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)    
    
    window.after(1000, update_clock)

    
canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.pack(expand=True, fill="both")

# create clock background
bg = tk.PhotoImage(file="dial_400.png")
canvas.create_image(200, 200, image=bg)

#Create clock hands
center_x = 200
center_y = 200
second_hand_len = 95
minutes_hand_len = 80
hours_hand_len = 60

#Drawing clock hands
second_hand = canvas.create_line(200, 200, 200 + second_hand_len, 200 + second_hand_len
                                , width=1.5, fill="red")
minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len
                                , width=2, fill="white")
hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len
                                , width=4, fill="white")

update_clock()
window.mainloop()