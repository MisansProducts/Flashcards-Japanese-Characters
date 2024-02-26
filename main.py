import tkinter as tk
import random

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
            "ら", "り", "る", "れ", "ろ",
            "や", "ゆ", "よ", "わ", "を",
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
            "ra", "ri", "ru", "re", "ro",
            "ya", "yu", "yo", "wa", "wo",
            "n"
        )
        self.character_label = tk.Label(root, font=("Helvetica", 128))
        self.romaji_label = tk.Label(root, font=("Helvetica", 96))
        self.time_label = tk.Label(root, font=("Courier New", 24))

    def update_character(self):
        random_character_1, random_character_2 = random.choice(list(zip(self.characters, self.romaji))) # Chooses a random character
        self.character_label.config(text=random_character_1)
        self.romaji_label.config(text=random_character_2)
        self.countdown(1000)
    
    def countdown(self, ms):
        if ms >= 0:
            self.time_label.config(text=str(round(ms / 1000, 1)))
            root.after(1, self.countdown, ms - 1)
        else:
            self.update_character()

# Create the main window
root = tk.Tk()
root.title("Flashcards")
root.geometry("800x450")

a = Main(root)
a.character_label.pack(expand=True)
a.romaji_label.pack()
a.time_label.pack()

a.update_character()

# Run the Tkinter event loop
root.mainloop()
