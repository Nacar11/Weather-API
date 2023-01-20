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
import os


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #setup
        self.geometry("900x600")
        self.title("Weather Checker Application")
        self.resizable(False, False)
        # self.configure(fg_color="#57adff")
        image_icon = PhotoImage(file=r"C:\Users\nacar\reposPython\WeatherAPI\icons\icon.png")
        self.iconphoto(False, image_icon)
        customtkinter.set_appearance_mode("dark")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        image_path = os.path.dirname(os.path.realpath(__file__))
        print(image_path)
        temp = "                   "
        humid = "                   "
        press = "                   "
        ws = "                   "
        desc = "                   "


        #initializing images
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path + "/icons/storm.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path + "/icons/storm.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path + "/icons/storm.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path + "/icons/storm.png")),
                                                 dark_image=Image.open(os.path.join(image_path + "/icons/storm.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path + "/icons/storm.png")),
                                                 dark_image=Image.open(os.path.join(image_path + "/icons/storm.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path + "/icons/storm.png")),
                                                     dark_image=Image.open(os.path.join(image_path + "/icons/storm.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=18)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label_time = customtkinter.CTkLabel(self.navigation_frame, text=" Time", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.navigation_frame_label_time.grid(row=0, column=0, padx=0, pady=(20,40))

        self.navigation_frame_label1 = customtkinter.CTkLabel(self.navigation_frame, text="Temperature" + temp,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label1.grid(row=1, column=0, sticky="ew", padx=20)

        self.navigation_frame_label2 = customtkinter.CTkLabel(self.navigation_frame, text="Humidity" + humid,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label2.grid(row=2, column=0, sticky="ew", padx=20)

        self.navigation_frame_label3 = customtkinter.CTkLabel(self.navigation_frame, text="Pressure" + press,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label3.grid(row=3, column=0, sticky="ew", padx=20)

        self.navigation_frame_label4 = customtkinter.CTkLabel(self.navigation_frame, text="Wind Speed" + ws,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label4.grid(row=4, column=0, sticky="ew", padx=20)

        self.navigation_frame_label4 = customtkinter.CTkLabel(self.navigation_frame, text="Description" + desc,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label4.grid(row=5, column=0, sticky="ew", padx=20)

        self.navigation_frame_label4 = customtkinter.CTkLabel(self.navigation_frame, text="" + desc,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label4.grid(row=6, column=0, sticky="ew", padx=20)

        


        # create main frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="asdasd", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

      # create right frame
        self.right_frame = customtkinter.CTkFrame(self, corner_radius=18)
        self.right_frame.grid(row=0, column=2, sticky="nsew")
        self.right_frame.grid_columnconfigure(0, weight=1)

        self.navigation_frame_label_time = customtkinter.CTkLabel(self.right_frame, text="",
                                                             compound="left", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.navigation_frame_label_time.grid(row=0, column=0, padx=0, pady=(20,40))


   

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
