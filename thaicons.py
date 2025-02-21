import tkinter as tk
import random

# List of Thai consonants and their names
THAI_CONSONANTS = [
    ("ก", "gor gai"), ("ข", "khor khai"), ("ฃ", "khor khuat"),
    ("ค", "khor khwai"), ("ฅ", "khor khon"), ("ฆ", "khor rakhang"),
    ("ง", "ngor ngu"), ("จ", "jor jaan"), ("ฉ", "chor ching"),
    ("ช", "chor chaang"), ("ซ", "sor so"), ("ฌ", "chor choe"),
    ("ญ", "yor ying"), ("ฎ", "dor cha-da"), ("ฏ", "tor pa-tak")
]

class ThaiFlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")
        
        self.current_card = None
        self.is_flipped = False
        
        self.card_label = tk.Label(root, text="", font=("Arial", 100), pady=20)
        self.card_label.pack()
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 14))
        self.flip_button.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14))
        self.next_button.pack(pady=10)
        
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(THAI_CONSONANTS)
        self.card_label.config(text=self.current_card[0])
        self.is_flipped = False
    
    def flip_card(self):
        if not self.is_flipped:
            self.card_label.config(text=self.current_card[1])
        else:
            self.card_label.config(text=self.current_card[0])
        self.is_flipped = not self.is_flipped

if __name__ == "__main__":
    root = tk.Tk()
    game = ThaiFlashcardGame(root)
    root.mainloop()
