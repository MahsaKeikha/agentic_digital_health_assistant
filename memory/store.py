class MemoryStore:
    def __init__(self):
        self.items = []

    def add(self, item: dict) -> None:
        self.items.append(item)
