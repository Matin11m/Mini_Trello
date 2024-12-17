class Card:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.status = "To Do"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        card = cls(data["title"], data.get("description", ""))
        card.status = data.get("status", "To Do")
        return card