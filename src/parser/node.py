from lexer.token import token


class node():
    def __init__(self, type: str, lit: token, *child) -> None:
        self.type: str = type
        self.ltype = lit.type
        self.lit = lit.lit
        self.child = list(child)

    def info(self, size: int = 0) -> None:
        print(' '*size+"|~ "+self.lit)
        for i in self.child:
            i.info(size+1)

    def append(self, obj) -> None:
        self.child.append(obj)
