from abstract_storage import AbstractStorage
from extensions import NotEnoughSpace, UnknownProduct, NotEnoughProduct


class Storage(AbstractStorage):

    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, title: str, quantity: int):
        if self.get_free_space() < quantity:
            raise NotEnoughSpace
        self._items[title] += quantity

    def remove(self, title: str, quantity: int):
        if title not in self._items:
            raise UnknownProduct
        if self._items[title] < quantity:
            raise NotEnoughProduct

        self._items[title] -= quantity
        if self._items[title] == 0:
            del self._items[title]

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
