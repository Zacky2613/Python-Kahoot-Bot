from kahoot import client
import tkinter as tk
from tkinter import messagebox
import socket, time




root = tk.Tk()
root.title("Kahoot Bot [v1.3.7]")
root.geometry("300x275")
root.iconbitmap('icon.ico')


# Gui part of the code
context = tk.Label(root, text=" Please enter all the infomation ")
context.pack(side = "top")

buffer = tk.Label(root, text=" ")
buffer.pack(side = "top", anchor = "nw")



room_key_label = tk.Label(root, text="Room Key:")
room_key_label.pack(side = "top", anchor = "nw")

room_key_entry = tk.Entry(root)
room_key_entry.pack(side = "top", anchor = "nw")

buffer2 = tk.Label(root, text=" ")
buffer2.pack(side = "top", anchor = "nw")



bot_name_input_label = tk.Label(root, text="Bot Name:")
bot_name_input_label.pack(side = "top", anchor = "nw")

bot_name_input_entry = tk.Entry(root, width = 25)
bot_name_input_entry.pack(side = "top", anchor = "nw")

buffer3 = tk.Label(root, text=" ")
buffer3.pack(side = "top", anchor = "nw")



bot_amount_label = tk.Label(root, text="Amount of Bots: ")
bot_amount_label.pack(side = "top", anchor = "nw")

bot_amount_entry = tk.Entry(root, width = 10)
bot_amount_entry.pack(side = "top", anchor = "nw")

buffer4 = tk.Label(root, text=" ")
buffer4.pack(side = "top", anchor = "nw")


bot_offset_label = tk.Label(root, text="Bot Joining offset (Best is 0.35): ")
bot_offset_label.pack(side = "top", anchor = "nw")

bot_offset_entry = tk.Entry(root, width = 5)
bot_offset_entry.pack(side = "top", anchor = "nw")

buffer5 = tk.Label(root, text=" ")
buffer5.pack(side = "top", anchor = "nw")




def kahoot_func(bind): 


    bot = client()

    # Checking if the entrys are correct with 
    try:
        room_key = int(room_key_entry.get())
        bot_name_input = bot_name_input_entry.get()
        bot_amount = int(bot_amount_entry.get())
        join_time = float(bot_offset_entry.get())
    
    except ValueError:
        messagebox.showerror("ERROR", "You must enter a number for the room key and bot amount.")

    bot_name_number_string_var = 0

    # Kahoot Bot Part
    try:
        for i in range(bot_amount):
            


            bot_name_number_string = str(bot_name_number_string_var + 1)
            bot_name = bot_name_input + " " + bot_name_number_string

            try:
                bot.join(room_key, bot_name)

            except:
                messagebox.showerror("ERROR", "Unable to join the room, either the room key is incorrect or the room is locked.")
            
            print(join_time)
            time.sleep(join_time)
            print(f"Joined [{room_key}]: {bot_name}")
            bot_name_number_string_var += 1


    except socket.gaierror:
        messagebox.showerror("ERROR", "You must be connected to the internet to use this.")
    
    except UnboundLocalError:
        #Does nothing lmaoooo
        time.sleep(0)


def close(bind):
    root.destroy()
    exit()



root.bind("<Return>", kahoot_func)
root.bind("<Escape>", close)

root.mainloop()



