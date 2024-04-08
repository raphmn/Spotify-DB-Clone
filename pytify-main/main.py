import customtkinter as ctk
import tkinter as tk

from PIL import Image
import ctypes

from app.player_frame import *
from app.navigator import *
from app.search import *

applicationID = 'nsi.project.spotify.1_0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(applicationID)

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1280x720')
        self.title('Spotify')
        self.iconbitmap('media/appicon/appicon.ico')

        self.navigator = LateralFrame(self, width=180, height=1080)
        self.navigator.pack(anchor=tk.NW, side="left")

        self.searchBar = SearchFrame(self, width=1050, height=170)
        
        self.test = ctk.CTkButton(self, command=self.show_search_bar)
        self.test.pack()

    def show_search_bar(self):

        self.searchBar.pack(anchor=tk.N)



app = App()
app.mainloop()
