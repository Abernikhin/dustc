class char():
    def __init__(self) -> None:
        self.type = ["number", "ptr"]
        self.name = []
        self.func = []

    def add_type(self, type: str) -> None:
        self.type.append(type)

    def get_type(self, type) -> bool:
        if type in self.type:
            return True
        return False

    def add_name(self, name: str) -> None:
        self.name.append(name)

    def get_name(self, name) -> bool:
        if name in self.name:
            return True
        return False
