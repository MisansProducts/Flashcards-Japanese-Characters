import tkinter as tk
from tkinter import ttk
import random
import time

class Main:
    def __init__(self, root: tk.Tk):
        self.characters = (
            "あ", "い", "う", "え", "お",
            "か", "き", "く", "け", "こ",
            "さ", "し", "す", "せ", "そ",
            "た", "ち", "つ", "て", "と",
            "な", "に", "ぬ", "ね", "の",
            "は", "ひ", "ふ", "へ", "ほ",
            "ま", "み", "む", "め", "も",
            "や", "ゆ", "よ",
            "ら", "り", "る", "れ", "ろ",
            "わ", "を",
            "ん"
        )
        self.romaji = (
            "a", "i", "u", "e", "o",
            "ka", "ki", "ku", "ke", "ko",
            "sa", "shi", "su", "se", "so",
            "ta", "chi", "tsu", "te", "to",
            "na", "ni", "nu", "ne", "no",
            "ha", "hi", "fu", "he", "ho",
            "ma", "mi", "mu", "me", "mo",
            "ya", "yu", "yo",
            "ra", "ri", "ru", "re", "ro",
            "wa", "wo",
            "n"
        )
        self.character_label = tk.Label(root, font=("Helvetica", 128))
        self.romaji_label = tk.Label(root, font=("Helvetica", 96))
        self.progress = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
        self.progress['maximum'] = 1000
        self.character_set = []

    def update_character(self):
        self.start_time = time.time()
        if not self.character_set:
            print("New Set")
            self.character_set = list(zip(self.characters, self.romaji))
            random.shuffle(self.character_set)
        random_character_1, random_character_2 = self.character_set.pop()
        self.character_label.config(text=random_character_1)
        self.romaji_label.config(text=random_character_2)
        self.progress['value'] = 1000 # Resets progress bar
        self.countdown()
        
    def countdown(self):
        elapsed_time = (time.time() - self.start_time) * 1000
        remaining_time = 1000 - elapsed_time

        if remaining_time > 0:
            self.progress['value'] = remaining_time # Updates progress bar
            root.after(10, self.countdown)
        else:
            self.update_character()

# Create the main window
root = tk.Tk()
root.title("Flashcards")
root.geometry("800x450")

a = Main(root)
a.character_label.pack(expand=True)
a.romaji_label.pack()
a.progress.pack(pady=20)

a.update_character()

# Run the Tkinter event loop
root.mainloop()
