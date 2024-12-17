from core.card import Card

class List:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def to_dict(self):
        return {
            "name": self.name,
            "cards": [card.to_dict() for card in self.cards]
        }

    @classmethod
    def from_dict(cls, data):
        lst = cls(data["name"])
        lst.cards = [Card.from_dict(card_data) for card_data in data["cards"]]
        return lst