from tkinter import messagebox
from kahoot import client
import tkinter as tk
import time

''' Python-Kahoot-Bot Copyright (c) 2022 Zacky2613 MIT License

    ███████╗ █████╗  ██████╗██╗  ██╗██╗   ██╗██████╗  ██████╗ ██╗██████╗ 
    ╚══███╔╝██╔══██╗██╔════╝██║ ██╔╝╚██╗ ██╔╝╚════██╗██╔════╝███║╚════██╗
      ███╔╝ ███████║██║     █████╔╝  ╚████╔╝  █████╔╝███████╗╚██║ █████╔╝
     ███╔╝  ██╔══██║██║     ██╔═██╗   ╚██╔╝  ██╔═══╝ ██╔═══██╗██║ ╚═══██╗
    ███████╗██║  ██║╚██████╗██║  ██╗   ██║   ███████╗╚██████╔╝██║██████╔╝
    ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝╚═════╝ 

Guthub Repo: https://github.com/Zacky2613/Python-Kahoot-Bot '''


def Kahoot_JoinLoop(game_pin, bot_name_input, bot_amount, join_time):

    bot = client()
    bot_name_number_string_var = -3
  
    print(f"Joining Server: {game_pin}")
    print("WARNING: bots will say 'connected' even if the game pin is invaild!\n")

    for i in range(bot_amount):
        bot_name_number_string = str(bot_name_number_string_var + 1)
        bot_name = bot_name_input + " " + bot_name_number_string

        bot.join(game_pin, bot_name) 

        bot.on('ready', print(f"Connected: {bot_name}"))    
        bot_name_number_string_var += 1
        time.sleep(join_time)

def Joinloop(bind):
    try:
        game_pin = int(room_key_entry.get())
        bot_name_input = bot_name_input_entry.get()
        bot_amount = int(bot_amount_entry.get())
        join_time = float(bot_offset_entry.get())

        Kahoot_JoinLoop(game_pin, bot_name_input, bot_amount, join_time)

    except ValueError:
        messagebox.showerror("ValueError", "ValueError: One of your inputs are wrong, only enter words for the username.")


if __name__ ==  "__main__":
    root = tk.Tk()
    root.title("Kahoot Bot [v1.5.3]")
    root.geometry("300x325")

    bot = client() 

    context = tk.Label(root, text=" Please enter all the infomation ").pack(side = "top")

    buffer = tk.Label(root, text=" ").pack(side = "top", anchor = "nw") # These buffers are used for seperating the input boxes to make it look cleaner.

    room_key_label = tk.Label(root, text="Room Key:").pack(side = "top", anchor = "nw")
    room_key_entry = tk.Entry(root).pack(side = "top", anchor = "nw")

    buffer2 = tk.Label(root, text=" ").pack(side = "top", anchor = "nw")

    bot_name_input_label = tk.Label(root, text="Bot Name:").pack(side = "top", anchor = "nw")
    bot_name_input_entry = tk.Entry(root, width = 25).pack(side = "top", anchor = "nw")

    buffer3 = tk.Label(root, text=" ").pack(side = "top", anchor = "nw")

    bot_amount_label = tk.Label(root, text="Amount of Bots: ").pack(side = "top", anchor = "nw")
    bot_amount_entry = tk.Entry(root, width = 10).pack(side = "top", anchor = "nw")

    buffer4 = tk.Label(root, text=" ").pack(side = "top", anchor = "nw")

    bot_offset_label = tk.Label(root, text="Bot Joining offset second: ").pack(side = "top", anchor = "nw")
    bot_offset_entry = tk.Entry(root, width = 5).pack(side = "top", anchor = "nw")

    buffer5 = tk.Label(root, text=" ").pack(side = "top", anchor = "nw")

    bot_join_button = tk.Button(root, text="Flood Kahoot Game", command=Joinloop).pack(side = "top", anchor = "nw")


    def close(bind):
        root.destroy()

    root.bind("<Return>", Joinloop)
    root.bind("<Escape>", close)

    root.mainloop()
