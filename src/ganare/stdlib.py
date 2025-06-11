memory = []


class var():
    def __init__(self) -> None:
        memory.append(0)
        self.lit = len(memory)-1

    def set(self, obj) -> None:
        memory[self.lit] = obj

    def get(self):
        return memory[self.lit]
