import tkinter as tk
from tkinter import ttk
import random
import time

class Main:
    def __init__(self, root: tk.Tk, diffuclty: int):
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
        self.difficulty = difficulty
        self.score = 0
        self.total = 0
        self.score_label = tk.Label(root, font=("Helvetica", 24), text="Accuracy: 0.00%")
        self.character_label = tk.Label(root, font=("Helvetica", 128))
        self.choice_frame = tk.Frame(root)
        self.choice1 = tk.Button(self.choice_frame, font=("Helvetica", 24), height=1, width=4)
        self.choice2 = tk.Button(self.choice_frame, font=("Helvetica", 24), height=1, width=4)
        self.choice3 = tk.Button(self.choice_frame, font=("Helvetica", 24), height=1, width=4)
        self.progress = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
        self.progress['maximum'] = 1000 * difficulty
        self.character_set = []
    
    def choose_character(self, expected, actual):
        if (expected == actual):
            self.score += 1
        self.update_character()

    def update_character(self):
        if self.total != 0:
            self.score_label.config(text=f"Accuracy: {(self.score / self.total) * 100:.2f}%")
        self.total += 1
        self.start_time = time.time()
        if not self.character_set:
            print("New Set")
            self.character_set = list(zip(self.characters, self.romaji))
            random.shuffle(self.character_set)
        hiragana_character, romaji_character = self.character_set.pop()
        choices = [romaji_character]
        while (len(choices) < 3):
            random_character = random.choice(self.romaji)
            if (random_character != romaji_character):
                choices.append(random_character)
        random.shuffle(choices)
        choice1, choice2, choice3 = choices
        self.character_label.config(text=hiragana_character)
        self.choice1.config(text=choice1, command=lambda: self.choose_character(romaji_character, choice1))
        self.choice2.config(text=choice2, command=lambda: self.choose_character(romaji_character, choice2))
        self.choice3.config(text=choice3, command=lambda: self.choose_character(romaji_character, choice3))
        self.progress['value'] = 1000 * self.difficulty # Resets progress bar
        self.countdown()
        
    def countdown(self):
        elapsed_time = (time.time() - self.start_time) * 1000
        remaining_time = 1000 * self.difficulty - elapsed_time

        if remaining_time > 0:
            self.progress['value'] = remaining_time # Updates progress bar
            root.after(10, self.countdown)
        else:
            self.update_character()

# Create the main window
root = tk.Tk()
root.title("Flashcards")
root.geometry("800x450")
difficulty = 2 # 2 seconds

a = Main(root, difficulty)
a.score_label.pack(anchor="e")
a.character_label.pack(expand=True)
a.choice1.grid(row=0, column=0)
a.choice2.grid(row=0, column=1)
a.choice3.grid(row=0, column=2)
a.choice_frame.pack()
a.progress.pack(pady=20)

a.update_character()

# Run the Tkinter event loop
root.mainloop()
