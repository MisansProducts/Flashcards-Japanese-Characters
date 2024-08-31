import tkinter as tk
from tkinter import ttk
import random
import time

class Main:
    def __init__(self, root: tk.Tk, diffuclty: int, num_choices: int):
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
        self.num_choices = num_choices
        self.score = 0
        self.total = 0
        self.score_label = tk.Label(root, font=("Helvetica", 24), text="Accuracy: 0.00%")
        self.character_label = tk.Label(root, font=("Helvetica", 128))
        self.choice_frame = tk.Frame(root)
        self.choices = [tk.Button(self.choice_frame, font=("Helvetica", 24), height=1, width=4) for _button in range(num_choices)]
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
        romajiCopy = list(self.romaji)
        random.shuffle(romajiCopy)
        while (len(choices) < num_choices):
            random_character = romajiCopy.pop()
            if (random_character != romaji_character):
                choices.append(random_character)
        random.shuffle(choices)
        [self.choices[i].config(text=choices[i], command=lambda i=i: self.choose_character(romaji_character, choices[i])) for i in range(num_choices)]
        self.character_label.config(text=hiragana_character)
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
num_choices = 3 # 3 buttons

a = Main(root, difficulty, num_choices)
a.score_label.pack(anchor="e")
a.character_label.pack(expand=True)
[a.choices[i].grid(row=0, column=i) for i in range(num_choices)]
a.choice_frame.pack()
a.progress.pack(pady=20)

a.update_character()

# Run the Tkinter event loop
root.mainloop()
