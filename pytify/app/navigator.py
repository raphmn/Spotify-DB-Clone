import customtkinter as ctk
import tkinter as tk

from PIL import Image

import vlc

idMusic = 19
# media object
media = vlc.Media(f'/media/songs/{idMusic}.mp3')
  
# setting media to the media player

media_player = vlc.MediaPlayer()
media_player.set_media(media)
media_player.set_media(media)

# Play to open/load the video

# Pause the Video

# Other Stuff Happens


class LateralFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        self.spotify_image_frame = ctk.CTkFrame(self, width=128, height=128)
        self.spotify_image_frame.pack(expand=True)

        self.cover_image = ctk.CTkImage(Image.open('media/covers/19.jpeg'), size=(128,128))
        self.cover_label = ctk.CTkLabel(self.spotify_image_frame, text='', image=self.cover_image)
        self.cover_label.pack()

        self.control_frame = ctk.CTkFrame(self)

        self.play_image = ctk.CTkImage(Image.open('media/play.png'), size=(32,32))
        self.play_buton = ctk.CTkButton(self.control_frame, fg_color='transparent', border_color='grey', width=25, height=25, image=self.play_image, text='', command= lambda: media_player.play())

        self.pause_image = ctk.CTkImage(Image.open('media/pause.png'), size=(32,32))
        self.pause_buton = ctk.CTkButton(self.control_frame, fg_color='transparent', border_color='grey', width=25, height=25, image=self.pause_image, text='', command= lambda: media_player.pause())

        self.control_frame.pack(pady=5, padx=5)

        self.play_buton.pack(pady=5, padx=5,side='left')
        self.pause_buton.pack(pady=5, padx=5,side='left')

        self.spotify_label = ctk.CTkLabel(self, text='')
        self.spotify_label.pack(expand=True)

        self.albums_image = ctk.CTkImage(Image.open('media/icons/albums_32.png'))
        self.albums_button = ctk.CTkButton(self, text='Albums',
                                           image=self.albums_image, command=self.change_album_display)
        self.albums_button.pack(ipadx=0, ipady=20, expand=True)

        self.artists_image = ctk.CTkImage(Image.open('media/icons/artists_32.png'))
        self.artists_button = ctk.CTkButton(self, text='Artists',
                                            image=self.artists_image, command=self.change_artist_display)
        self.artists_button.pack(ipadx=0, ipady=20, expand=True)

        self.search_image = ctk.CTkImage(Image.open('media/icons/search_32.png'))
        self.search_button = ctk.CTkButton(self, text='Search',
                                           image=self.search_image, command=self.change_search_display)
        self.search_button.pack(ipadx=0, ipady=20, expand=True)

        self.search_button_display = tk.BooleanVar()
        self.albums_button_display = tk.BooleanVar()
        self.artists_button_display = tk.BooleanVar()

    def change_search_display(self):
        self.search_button_display.set((True if not self.search_button_display.get() else False))

    def change_album_display(self):
        self.albums_button_display.set((True if not self.albums_button_display.get() else False))

    def change_artist_display(self):
        self.artists_button_display.set((True if not self.artists_button_display.get() else False))




