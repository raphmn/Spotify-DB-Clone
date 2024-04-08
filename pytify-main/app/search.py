import customtkinter as ctk
import tkinter as tk

from PIL import Image

class SearchFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)

        self.search = tk.StringVar()

        self.searchBar = ctk.CTkEntry(self, placeholder_text="Rechercher", width=550, height=70, corner_radius=8, font=('Segoe UI', 18))
        self.searchBar.pack(anchor=tk.CENTER, side=tk.LEFT, )

        self.deleteButton = ctk.CTkButton(self, text='X', fg_color='transparent', command=self.reset_search_bar)
        self.deleteButton.pack(side=tk.LEFT, expand=True)

    def reset_search_bar(self):
        self.search.set('')