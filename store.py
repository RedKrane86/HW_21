from storage import Storage


class Store(Storage):

    def __init__(self, title: dict, capacity: int = 100):
        super().__init__(title, capacity)




