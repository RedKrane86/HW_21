from extensions import TooManyDifferentProducts
from storage import Storage


class Shop(Storage):
    def __init__(self, title: dict, capacity: int = 20):
        super().__init__(title, capacity)

    def add(self, title: str, quantity: int):
        if title not in self.get_items() and self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts
        super().add(title, quantity)
