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
        self.geometry("600x600")
        self.title("Weather Checker Application")
        self.resizable(False, False)
        # self.configure(fg_color="#57adff")
        image_icon = PhotoImage(file=r"C:\Users\nacar\reposPython\WeatherAPI\icons\icon.png")
        self.iconphoto(False, image_icon)
        customtkinter.set_appearance_mode("dark")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        image_path = os.path.dirname(os.path.realpath(__file__))
        print(image_path)
        sep1="                   "
        sep2="                                      "
        temp = ""
        humid = ""
        press = ""
        ws = ""
        desc = ""
        prev = ""
        nxt = ""
        nxt1 = ""


        #initializing images
        self.main_image = customtkinter.CTkImage(Image.open(os.path.join(image_path + "/icons/snowy.png")), size=(140, 150))
        self.loc_image = customtkinter.CTkImage(Image.open(os.path.join(image_path + "/icons/place.png")), size=(26, 26))
        self.time_image= customtkinter.CTkImage(Image.open(os.path.join(image_path + "/icons/clock.png")), size=(26, 26))
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
        self.navigation_frame.grid_rowconfigure(10, weight=1)

        self.navigation_frame_label_time = customtkinter.CTkLabel(self.navigation_frame, text=" 10:41 AM",
                                                             compound="left", font=customtkinter.CTkFont(size=30))
        self.navigation_frame_label_time.grid(row=0, column=0, padx=0, pady=(20,8))

        self.navigation_frame_label_loc = customtkinter.CTkLabel(self.navigation_frame, text=" Singapore/Asia", image=self.loc_image,
                                                             compound="left", font=customtkinter.CTkFont(size=25))
        self.navigation_frame_label_loc.grid(row=1, column=0, padx=12, pady=(20,80))

        self.navigation_frame_label1 = customtkinter.CTkLabel(self.navigation_frame, text="Temperature"+sep1+temp,
                                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.navigation_frame_label1.grid(row=2, column=0, sticky="ew", padx=20)

        self.navigation_frame_label2 = customtkinter.CTkLabel(self.navigation_frame, text="Humidity" +sep1+humid,
                                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.navigation_frame_label2.grid(row=3, column=0, sticky="ew", padx=20)

        self.navigation_frame_label3 = customtkinter.CTkLabel(self.navigation_frame, text="Pressure"+sep1+press,
                                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.navigation_frame_label3.grid(row=4, column=0, sticky="ew", padx=20)

        self.navigation_frame_label4 = customtkinter.CTkLabel(self.navigation_frame, text="Wind Speed"+sep1+ws,
                                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.navigation_frame_label4.grid(row=5, column=0, sticky="ew", padx=20)

        self.navigation_frame_label4 = customtkinter.CTkLabel(self.navigation_frame, text="Description"+sep1+desc,
                                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.navigation_frame_label4.grid(row=6, column=0, sticky="ew", padx=20)

        self.navigation_frame_label4 = customtkinter.CTkLabel(self.navigation_frame, text="" + desc,
                                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.navigation_frame_label4.grid(row=7, column=0, sticky="ew", padx=20)

        


        # create main frame
        
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="Location")
        self.entry.focus_set()
        self.entry.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")
        

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.main_image)
        self.home_frame_large_image_label.grid(row=1, column=0, padx=0, pady=10)

        self.home_frame_label1 = customtkinter.CTkLabel(self.home_frame, text="  -31° ", font=customtkinter.CTkFont(size=45, weight="bold"))
        self.home_frame_label1.grid(row=2, column=0, padx=0, pady=0)
        self.home_frame_label2 = customtkinter.CTkLabel(self.home_frame, text="snowy ", font=customtkinter.CTkFont(size=13))
        self.home_frame_label2.grid(row=3, column=0, padx=0, pady=(0,70))
        self.home_frame_label2 = customtkinter.CTkLabel(self.home_frame, text="Tuesday "+sep2+sep1+prev, font=customtkinter.CTkFont(size=13))
        self.home_frame_label2.grid(row=4, column=0, padx=0, pady=0)
        self.home_frame_label2 = customtkinter.CTkLabel(self.home_frame, text="Thursday"+sep2+sep1+nxt, font=customtkinter.CTkFont(size=13))
        self.home_frame_label2.grid(row=5, column=0, padx=0, pady=0)
        self.home_frame_label2 = customtkinter.CTkLabel(self.home_frame, text="Friday"+sep2+sep1+nxt1, font=customtkinter.CTkFont(size=13))
        self.home_frame_label2.grid(row=6, column=0, padx=0, pady=0)

        

    #   # create right frame
    #     self.right_frame = customtkinter.CTkFrame(self, corner_radius=18)
    #     self.right_frame.grid(row=0, column=2, sticky="nsew")
    #     self.right_frame.grid_columnconfigure(0, weight=1)

    #     self.navigation_frame_label_time = customtkinter.CTkLabel(self.right_frame, text="",
    #                                                          compound="left", font=customtkinter.CTkFont(size=30, weight="bold"))
    #     self.navigation_frame_label_time.grid(row=0, column=0, padx=0, pady=(20,40))


   

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
