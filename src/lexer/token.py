class token():
    def __init__(self, _type: str, lit: str) -> None:
        self.type = _type
        self.lit = lit

    def info(self) -> None:
        print(f"{self.type}: {self.lit};")
