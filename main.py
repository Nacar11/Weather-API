from tkinter import *
import tkinter as tk
import customtkinter 
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("890x470+300+300")
        self.title("Weather Checker Application")
        self.resizable(False, False)
        self.configure(fg_color="#57adff")
        image_icon = PhotoImage(file=r"C:\Users\nacar\reposPython\WeatherAPI\icons\icon.png")
        self.iconphoto(False, image_icon)

    
    




def main():
    app = App()
    app.mainloop()


main()