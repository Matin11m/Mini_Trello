import tkinter as tk
from tkinter import ttk, messagebox
from core.board import Board
from core.list import List
from core.card import Card

class TrelloApp(tk.Tk):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.title("Mini Trello")
        self.geometry("800x600")
        self.list_frames = []
        self.create_widgets()

    def create_widgets(self):
        for lst in self.board.lists:
            self.create_list_frame(lst)

        add_list_button = ttk.Button(self, text="Add List", command=self.add_new_list)
        add_list_button.pack(pady=10)

    def create_list_frame(self, lst):
        frame = ttk.Frame(self, padding=10, borderwidth=2, relief="groove")
        frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        list_label = ttk.Label(frame, text=lst.name, font=("Arial", 14, "bold"))
        list_label.pack()

        card_frame = ttk.Frame(frame)
        card_frame.pack(fill=tk.BOTH, expand=True)

        for card in lst.cards:
            self.create_card_label(card_frame, card)

        add_card_button = ttk.Button(frame, text="Add Card", command=lambda l=lst: self.add_new_card(l))
        add_card_button.pack(pady=5)
        self.list_frames.append((frame, card_frame))

    def create_card_label(self, parent, card):
        card_label = ttk.Label(parent, text=card.title, borderwidth=1, relief="solid", padding=5, wraplength=150)
        card_label.pack(fill=tk.X, pady=2)

    def add_new_list(self):
        def save_list():
            list_name = entry.get()
            if list_name:
                self.board.add_list(List(list_name))
                self.create_list_frame(self.board.lists[-1])
                popup.destroy()
            else:
                messagebox.showerror("Error", "List name cannot be empty.")

        popup = tk.Toplevel(self)
        popup.title("New List")
        entry = ttk.Entry(popup)
        entry.pack(padx=10, pady=5)
        save_button = ttk.Button(popup, text="Save", command=save_list)
        save_button.pack(pady=5)

    def add_new_card(self, lst):
        def save_card():
            card_title = title_entry.get()
            card_description = description_entry.get("1.0", tk.END)
            if card_title:
                lst.add_card(Card(card_title, card_description))
                frame, card_frame = self.list_frames[self.board.lists.index(lst)]
                self.create_card_label(card_frame, lst.cards[-1])
                popup.destroy()
            else:
                messagebox.showerror("Error", "Card title cannot be empty.")

        popup = tk.Toplevel(self)
        popup.title("New Card")

        title_label = ttk.Label(popup, text="Title:")
        title_label.grid(row=0, column=0, padx=5, pady=2)
        title_entry = ttk.Entry(popup)
        title_entry.grid(row=0, column=1, padx=5, pady=2)

        description_label = ttk.Label(popup, text="Description:")
        description_label.grid(row=1, column=0, padx=5, pady=2)
        description_entry = tk.Text(popup, height=3)
        description_entry.grid(row=1, column=1, padx=5, pady=2)

        save_button = ttk.Button(popup, text="Save", command=save_card)
        save_button.grid(row=2, column=0, columnspan=2, pady=5)