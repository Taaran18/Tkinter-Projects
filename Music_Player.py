import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player App")

        self.playlist = []
        self.current_song_index = 0

        self.play_button = tk.Button(root, text="Play", command=self.play_song)
        self.play_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_song)
        self.pause_button.pack()

        self.resume_button = tk.Button(root, text="Resume", command=self.resume_song)
        self.resume_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_song)
        self.stop_button.pack()

        self.load_button = tk.Button(root, text="Load Song", command=self.load_song)
        self.load_button.pack()

    def play_song(self):
        if not pygame.mixer.get_busy():
            pygame.mixer.music.load(self.playlist[self.current_song_index])
            pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def resume_song(self):
        pygame.mixer.music.unpause()

    def stop_song(self):
        pygame.mixer.music.stop()

    def load_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.playlist.append(file_path)

if __name__ == "__main__":
    pygame.mixer.init()
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
