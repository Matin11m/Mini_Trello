from core.list import List

class Board:
    def __init__(self, name):
        self.name = name
        self.lists = []

    def add_list(self, lst):
        self.lists.append(lst)

    def to_dict(self):
        return {
            "name": self.name,
            "lists": [lst.to_dict() for lst in self.lists]
        }

    @classmethod
    def from_dict(cls, data):
        board = cls(data["name"])
        board.lists = [List.from_dict(list_data) for list_data in data["lists"]]
        return board