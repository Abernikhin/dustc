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

    def parsing(self):
        while self.tokens.__len__() > 0:
            self.let()
        return [self.reslut, self.char]

    def let(self) -> None:
        if self.tokens[0].lit == ';':
            self.semi()
        elif self.char.get_type(self.tokens[0].lit):
            self.reslut.append(node("var type", self.tokens[0]))
            if self.tokens[1].type == "name":
                if self.tokens[2].lit == '(':
                    funcl = [self.tokens[1].lit]
                    func = []
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
                    index = 1
                    while True:
                        if self.tokens[index].lit == ')':
                            break
                        if self.tokens != ',' and self.char.get_type(
                            self.tokens[index].lit
                                                                     ):
                            func.append(
                                node("op",
                                     self.tokens[index+1],
                                     node("op", self.tokens[index])
                                     )
                                )
                        index += 1
                    for i in range(0, index):
                        self.tokens.pop(1)
                    self.char.add_func(tuple(funcl))
                    self.reslut.append(
                        node("var type", self.tokens[0], node(
                            "func name",
                            token(
                                "name",
                                self.char.func[-1][0]
                                )
                            )
                        ))
                    for i in func:
                        self.reslut[-1].child[-1].append(i)
                    
                else:
                    if self.char.get_name(self.tokens[1].lit):
                        raise parser_double_init()
                    if self.tokens[2].type == "index":
                        self.char.add_name(self.tokens[1].lit,
                                           self.tokens[0].lit
                                           )
                        self.reslut[-1].append(
                            node(
                                "arr name", self.tokens[1], node("size", self.tokens[2])
                                 )
                                               )
                        self.tokens.pop(1)
                        self.tokens.pop(1)
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
                self.reslut.append(node("new", self.tokens[1]))
                self.tokens.pop(1)
            elif self.tokens[1].lit == ';':
                self.tokens.pop(0)
                self.semi()
        else:
            self.eq()

    def eq(self) -> None:
        if self.tokens[0].lit == ';':
            self.semi()
        if self.tokens[1].lit == '=':
            self.reslut.append(node("eq", self.tokens[1], self.mname()))
            self.tokens.pop(0)
            self.reslut[-1].append(self.math())
            self.semi()
        elif self.tokens[2].lit == '=':
            self.reslut.append(node("eq", self.tokens[2], self.mname()))
            self.tokens.pop(0)
            self.reslut[-1].append(self.math())
            self.semi()
        else:
            self.call()

    def semi(self) -> None:
        try:
            if self.tokens[0].lit == ';':
                self.reslut.append(node("new", self.tokens[0]))
                self.tokens.pop(0)
            else:
                for i in self.tokens:
                    i.info()
                raise parser_havent_semicolon()
        except IndexError:
            self.reslut.append(node("new", token("semicolon", ';')))

    def call(self) -> None:
        if self.tokens[0].lit == ';':
            self.semi()
        elif self.tokens[1].lit == '(':
            self.reslut.append(self.math())
            self.semi()
        else:
            self.semi()

    def mname(self) -> node:
        if self.tokens[0].lit == "&":
            n = node(
                        "op", self.tokens[0], node(
                                    "ptr",
                                    self.tokens[1],
                                    )
                                )
            self.tokens.pop(0)
            self.tokens.pop(0)
            return n
        if self.tokens[1].type == "index":
            n = node("op", self.tokens[1], node("op", self.tokens[0]))
            self.tokens.pop(0)
            self.tokens.pop(0)
            return n
        n = node("op", self.tokens[0])
        self.tokens.pop(0)
        return n

    def math(self) -> node:
        if self.tokens[0].lit == ',':
            self.tokens.pop(0)
        if self.tokens[0].type == "operator++":
            n = node("incr", self.tokens[0])
            self.tokens.pop(0)
            return n
        if self.tokens[0].type == "operator--":
            n = node("decr", self.tokens[0])
            self.tokens.pop(0)
            return n
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
            self.tokens.pop(0)
            if self.tokens[1].lit == "+" or self.tokens[1].lit == "-":
                n = node("func",
                         self.tokens[1],
                         node(
                             "op", s, node(
                                  "ptr",
                                  self.tokens[0]
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
        if self.tokens[1].lit == '(':
            n = node("call", self.tokens[0])
            self.tokens.pop(0)
            self.tokens.pop(0) 
            while self.tokens[0].lit != ')':
                n.append(self.math())
            self.tokens.pop(0)
            return n
        if self.tokens[1].type == 'index':
            n = node("op", self.tokens[1], node("op", self.tokens[0]))
            self.tokens.pop(0)
            self.tokens.pop(0)
            return n
        if self.tokens[1].lit == ';':
            n = node("op", self.tokens[0])
            self.tokens.pop(0)
            return n
        n = node("op", self.tokens[0])
        self.tokens.pop(0)
        n.append(self.math())
        return n
