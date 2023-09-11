import tkinter as tk
from tkinter import messagebox

class MusicPlaylistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Playlist App")

        self.playlist = []

        self.song_label = tk.Label(root, text="Song:")
        self.song_label.pack()

        self.song_entry = tk.Entry(root)
        self.song_entry.pack()

        self.add_button = tk.Button(root, text="Add Song", command=self.add_song)
        self.add_button.pack()

        self.playlist_listbox = tk.Listbox(root)
        self.playlist_listbox.pack()

        self.remove_button = tk.Button(root, text="Remove Song", command=self.remove_song)
        self.remove_button.pack()

    def add_song(self):
        song = self.song_entry.get()
        if song:
            self.playlist.append(song)
            self.update_listbox()
            self.song_entry.delete(0, tk.END)

    def remove_song(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.playlist[index]
            self.update_listbox()

    def update_listbox(self):
        self.playlist_listbox.delete(0, tk.END)
        for song in self.playlist:
            self.playlist_listbox.insert(tk.END, song)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlaylistApp(root)
    root.mainloop()
