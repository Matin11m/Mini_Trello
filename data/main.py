import json
import os
from core.board import Board
from core.list import List
from core.card import Card
from ui.cli import handle_user_input
from ui.gui import TrelloApp

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "board_data.json")

def save_board(board):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(board.to_dict(), f, indent=4)

def load_board():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return Board.from_dict(data)
    except FileNotFoundError:
        return None

def main():
    loaded_board = load_board()

    if loaded_board is None:
        my_board = Board("My Project")
        todo_list = List("To Do")
        doing_list = List("Doing")
        done_list = List("Done")

        my_board.add_list(todo_list)
        my_board.add_list(doing_list)
        my_board.add_list(done_list)

        card1 = Card("Task 1", "Description of task 1")
        card2 = Card("Task 2")
        card3 = Card("Task 3", "description of task 3")

        todo_list.add_card(card1)
        doing_list.add_card(card2)
        done_list.add_card(card3)

        save_board(my_board)
        print("New board created")
    else:
        my_board = loaded_board
        print("Board loaded from file")

    while True:
        print("\nChoose interface:")
        print("1. Command-Line Interface (CLI)")
        print("2. Graphical User Interface (GUI)")
        choice = input("> ")

        if choice == "1":
            my_board = handle_user_input(my_board)
            break
        elif choice == "2":
            app = TrelloApp(my_board)
            app.mainloop()
            break
        else:
            print("Invalid choice. Please try again.")

    save_board(my_board)

if __name__ == "__main__":
    main()