from kahoot import client
import tkinter as tk
from tkinter import messagebox
import socket, time

'''
    Copyright (c) Python-Kahoot-Bot 2021 Zacky2613
    
    P.S: Sorry if the code is hard to read, I'm trying to figure out
    how to get some functions to work like I want it to and once I get
    that done I'll go back and make the code easier to read.
'''

def Kahoot_JoinLoop(game_pin, bot_name_input, bot_amount, join_time):

    bot = client()
    bot_name_number_string_var = -3

    try:    
        print(f"Joining Server: {game_pin}\n")
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


    bot_offset_label = tk.Label(root, text="Bot Joining offset second: ")
    bot_offset_label.pack(side = "top", anchor = "nw")
 

    bot_offset_entry = tk.Entry(root, width = 5)
    bot_offset_entry.pack(side = "top", anchor = "nw")

    buffer5 = tk.Label(root, text=" ")
    buffer5.pack(side = "top", anchor = "nw")



    bot = client() 


    def Joinloop(bind):
        try:
            # Grabs the user inputs.
            game_pin = int(room_key_entry.get())
            bot_name_input = bot_name_input_entry.get()
            bot_amount = int(bot_amount_entry.get())
            join_time = float(bot_offset_entry.get())
            # Puts the inputs into the bot spamming func
            Kahoot_JoinLoop(game_pin, bot_name_input, bot_amount, join_time)

        except ValueError:
            # If one of the inputs are wrong (E.G: they put "banana" in the Game Pin) it will give a error
            messagebox.showerror("ValueError", "ValueError: One of your inputs are wrong, only enter words for the username.")


            
    def close(bind):
        root.destroy()
        exit()

    def recon(bind):
        bot.reconnect()
        



    root.bind("<Return>", Joinloop)
    root.bind("<Escape>", close)
    root.bind("<Alt-s>", recon)

    root.mainloop()
