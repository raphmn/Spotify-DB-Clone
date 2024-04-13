import customtkinter as ctk
import tkinter as tk

from PIL import Image


class SearchFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.search = tk.StringVar()

        self.search_bar = ctk.CTkEntry(self, placeholder_text="Rechercher", width=550, height=60, corner_radius=8,
                                       font=('Segoe UI', 18), textvariable=self.search)
        self.search_bar.pack(expand=True, anchor=tk.N, side=tk.LEFT, pady=25)