import tkinter, time, webbrowser
import customtkinter as ct
from PIL import ImageTk, Image

ct.set_appearance_mode("System")
ct.set_default_color_theme("green")

#pencere hakkında
pencere = ct.CTk()
pencere.geometry("600x600")
pencere.title("Coin Life Simulation")

#coin secme
def btc_komut():
    global cerceve
    cerceve = ct.CTkFrame(master=pencere, width=470, height=550, fg_color="grey")
    cerceve.place(relx=0.59, rely=0.47, anchor=tkinter.CENTER)

    satın_al = ct.CTkButton(master=cerceve, height=40, width=210, text="Satın Al", fg_color="green", hover_color="darkgreen")
    satın_al.place(relx=0.75, rely=0.93, anchor=tkinter.CENTER)

    sat = ct.CTkButton(master=cerceve, height=40, width=210, text="Sat", fg_color="red", hover_color="darkred")
    sat.place(relx=0.27, rely=0.93, anchor=tkinter.CENTER)

    derece = ct.CTkSlider(master=cerceve, width=360)
    derece.place(relx=0.5, rely=0.83, anchor=tkinter.CENTER)

    cerceve_ici = ct.CTkFrame(master=cerceve, width=450, height=410, fg_color="darkgrey")
    cerceve_ici.place(relx=0.5, rely=0.395, anchor=tkinter.CENTER)

def eth_komut():
    print(1)

def bnb_komut():
    print(1)


ana_coin_frame = ct.CTkFrame(master=pencere, width=101, height=550, fg_color="darkgrey")
ana_coin_frame.place(relx=0.1, rely=0.47, anchor=tkinter.CENTER)

btc = ct.CTkButton(master= ana_coin_frame, width=100, height=23, command=btc_komut, fg_color="yellow", 
                       hover_color="#8b795e", text="BTC", text_color="black", corner_radius=4)
btc.place(relx=0.5, rely=0.03, anchor=tkinter.CENTER, )

eth = ct.CTkButton(master= ana_coin_frame, width=100, height=23, command=eth_komut, fg_color="yellow", 
                       hover_color="#8b795e", text="ETH", text_color="black", corner_radius=4)
eth.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER, )

bnb = ct.CTkButton(master= ana_coin_frame, width=100, height=23, command=bnb_komut, fg_color="yellow", 
                       hover_color="#8b795e", text="BNB", text_color="black", corner_radius=4)
bnb.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER, )

#alt kılavuz
alt_kılavuz = ct.CTkFrame(master=pencere, height=40, width=650, fg_color="grey")
alt_kılavuz.place(relx=0.5, rely=0.971, anchor=tkinter.CENTER)

ana_menu = ct.CTkButton(master=pencere, height=30)

pencere.mainloop()