from core.board import Board
from core.list import List
from core.card import Card

def display_board(board):
    print("-" * 30)
    print(f"Board: {board.name}")
    print("-" * 30)
    for lst in board.lists:
        print(f"\nList: {lst.name}")
        if lst.cards:
            for card in lst.cards:
                print(f"  - {card.title} ({card.status})")
        else:
            print("  No cards in this list.")
    print("-" * 30)

def get_user_input(prompt):
    return input(prompt).strip()

def handle_user_input(board):
    while True:
        display_board(board)
        print("\nChoose an action:")
        print("1. Add a list")
        print("2. Add a card to a list")
        print("3. Exit")

        choice = get_user_input("> ")

        if choice == "1":
            list_name = get_user_input("Enter list name: ")
            board.add_list(List(list_name))
        elif choice == "2":
            display_board(board)
            try:
                list_index = int(get_user_input("Enter the list number to add card to: ")) - 1
                if 0 <= list_index < len(board.lists):
                    card_title = get_user_input("Enter card title: ")
                    card_description = get_user_input("Enter card description (optional): ")
                    board.lists[list_index].add_card(Card(card_title, card_description))
                else:
                    print("Invalid list number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
    return board