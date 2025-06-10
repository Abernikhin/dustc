from parser.node import node, token
from parser.char import char


class parser_double_init(Exception):
    pass


class parser_wrong_syntax(Exception):
    pass


class parser_eq(Exception):
    pass


class parser_havent_semicolon(Exception):
    pass


class parser():
    def __init__(self, tokens: list[token]) -> None:
        self.tokens = tokens
        self.char = char()
        self.reslut: list[node] = []

    def parsing(self) -> list[node]:
        while self.tokens.__len__() > 0:
            self.let()
        return self.reslut

    def let(self) -> None:
        if self.char.get_type(self.tokens[0].lit):
            self.reslut.append(node("var type", self.tokens[0]))
            if self.tokens[1].type == "name":
                if self.tokens[2].lit == '(':
                    funcl = [self.tokens[1].lit]
                    self.tokens.pop(1)
                    self.tokens.pop(1)
                    index = 1
                    while True:
                        if self.tokens[index].lit == ')':
                            break
                        if self.tokens != ',' and self.char.get_type(
                            self.tokens[index].lit
                                                                     ):
                            funcl.append(self.tokens[index].lit)
                        index += 1
                    for i in range(0, index):
                        self.tokens.pop(1)
                    self.char.add_func(tuple(funcl))
                    self.reslut.append(
                        node("type", self.tokens[0], node(
                            "func name",
                            token(
                                "name",
                                self.char.func[-1][0]
                                )
                            )
                        ))
                    for i in range(1, len(self.char.func[-1])):
                        self.reslut[-1].child[-1].append(node("op", token(
                                            "",
                                            self.char.func[-1][i])
                                                    )
                                               )
                else:
                    if self.char.get_name(self.tokens[1].lit):
                        raise parser_double_init()
                    else:
                        self.char.add_name(self.tokens[1].lit,
                                           self.tokens[0].lit
                                           )
                        self.reslut[-1].append(
                            node(
                                "var name", self.tokens[1]
                                 )
                                               )
                        self.tokens.pop(1)
            else:
                raise parser_wrong_syntax()
            if self.tokens[1].lit == ',':
                self.tokens.pop(1)
            elif self.tokens[1].lit == ';':
                self.tokens.pop(0)
                self.semi()
        else:
            self.eq()

    def eq(self) -> None:
        if self.tokens[1].lit == '=':
            if self.tokens[0].type != "name":
                raise parser_eq()
            self.reslut.append(
                node(
                    "eq",
                    self.tokens[1],
                    node(
                        "name",
                        self.tokens[0]
                        )
                    )
                )
            self.tokens.pop(0)
            self.tokens.pop(0)
            self.reslut[-1].append(self.math())
            self.semi()
        else:
            self.call()

    def call(self) -> None:
        if self.tokens[1].lit == "(":
            self.reslut.append(node("call", self.tokens[0]))
            index = 2
            while True:
                if self.tokens[index].lit == ')':
                    break
                if self.tokens[index].lit != ',':
                    self.reslut[-1].append(node("op", self.tokens[index]))
                index += 1
            for i in range(0, index+1):
                self.tokens.pop(0)
            self.semi()

    def semi(self) -> None:
        if self.tokens[0].lit == ';':
            self.reslut.append(node("new", self.tokens[0]))
            self.tokens.pop(0)
        else:
            raise parser_havent_semicolon()

    def math(self) -> node:
        if self.tokens[1].lit == "+" or self.tokens[1].lit == "-":
            n = node("func", self.tokens[1], node("op", self.tokens[0]))
            self.tokens.pop(0)
            self.tokens.pop(0)
            n.append(self.math())
            return n
        elif self.tokens[1].lit == "*" or self.tokens[1].lit == "/":
            n = node("func", self.tokens[1], node("op", self.tokens[0]))
            self.tokens.pop(0)
            self.tokens.pop(0)
            n.append(self.math())
            return n
        elif self.tokens[0].lit == "&":
            s = self.tokens[0]
            s.info()
            self.tokens.pop(0)
            if self.tokens[1].lit == "+" or self.tokens[1].lit == "-":
                n = node("func",
                         self.tokens[1],
                         node(
                             "op", s, node(
                                  "ptr",
                                  self.tokens[0],
                                  )
                              )
                         )
                self.tokens.pop(0)
                self.tokens.pop(0)
                n.append(self.math())
                return n
            if self.tokens[1].lit == "*" or self.tokens[1].lit == "/":
                n = node("func",
                         self.tokens[1],
                         node(
                             "op", s, node(
                                  "ptr",
                                  self.tokens[0],
                                  )
                              )
                         )
                self.tokens.pop(0)
                self.tokens.pop(0)
                n.append(self.math())
                return n
            n = node(
                             "op", s, node(
                                  "ptr",
                                  self.tokens[0],
                                  )
                              )
            self.tokens.pop(0)
            return n
        n = node("op", self.tokens[0])
        self.tokens.pop(0)
        return n
