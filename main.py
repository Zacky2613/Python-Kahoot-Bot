from kahoot import client             # Imports kahoot client (what we'll use for botting)
import tkinter as tk                  # This is made for the GUI 
from tkinter import messagebox        # If you forget to fill a input (entry box) it will alert you with a error pop up
import socket, time                   # The time is used for the offset that the bots join

"""
    Code made by Zacky2613 (c) 2021
    
    Fun Fact: KahootPY breaks Kahoot.it so your username can be whatever length it wants!
    + If the game owner makes it so you muse a friendly username with the spinner this alsom bypasses it to!
"""


# This is the function that will bot the game
def Kahoot_JoinLoop(game_pin, bot_name_input, bot_amount, join_time):

    bot = client()
    bot_name_number_string_var = -3

    try:    
        print(f"Joining Server: {game_pin}")
        print("WARNING: bots will say 'connected' even if the game pin is invaild!\n")
        for i in range(bot_amount):

            bot_name_number_string = str(bot_name_number_string_var + 1)
            bot_name = bot_name_input + " " + bot_name_number_string

            try:
                bot.join(game_pin, bot_name) 

            except:
                messagebox.showerror("ERROR", "Unable to join the room, either the room key is incorrect or the room is locked.")


            bot.on('ready', print(f"Connected: {bot_name}"))    
            bot_name_number_string_var += 1
            time.sleep(join_time)


    except (ValueError, UnboundLocalError):
        messagebox.showerror("ValueError", "ValueError: One of the inputs of entered was wrong")




if __name__ ==  "__main__":

    root = tk.Tk()
    root.title("Kahoot Bot [v1.5.3]")
    root.geometry("300x325")
    # root.iconbitmap('icon.ico')


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


    bot_offset_label = tk.Label(root, text="Bot Joining offset second: ")
    bot_offset_label.pack(side = "top", anchor = "nw")


    bot_offset_entry = tk.Entry(root, width = 5)
    bot_offset_entry.pack(side = "top", anchor = "nw")

    buffer5 = tk.Label(root, text=" ")
    buffer5.pack(side = "top", anchor = "nw")



    bot = client() 


    def Joinloop(bind):
        try:
            game_pin = int(room_key_entry.get())
            bot_name_input = bot_name_input_entry.get()
            bot_amount = int(bot_amount_entry.get())
            join_time = float(bot_offset_entry.get())
            Kahoot_JoinLoop(game_pin, bot_name_input, bot_amount, join_time)

        except ValueError:
            messagebox.showerror("ValueError", "ValueError: One of your inputs are wrong, only enter words for the username.")
        

    def close(bind):
        root.destroy()
        




    root.bind("<Return>", Joinloop)
    root.bind("<Escape>", close)

    root.mainloop()
