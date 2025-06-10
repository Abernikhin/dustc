import re
from lexer.token import token


class wrong_token_error(Exception):
    pass


class lexer():
    def __init__(self, code: str) -> None:
        self.code: str = code
        self.rules: dict = {
            "num": r"(\d+)",
            "name": r"([\w\d\_]+)",
            "comma": r"(\,)",
            "semicolon": r"(\;)",
            "eq": r"(\=)",
            "operator+": r"(\+)",
            "operator-": r"(\-)",
            "operator*": r"(\*)",
            "operator/": r"(\/)",
            "operator&": r"(\&)",
            "open": r"(\()",
            "close": r"(\))",
            "skip": r"(\s+)",
        }

    def reline(self, obj: str) -> None:
        result = ""
        for i in range(len(obj), len(self.code)):
            result += self.code[i]

        self.code = result

    def tokenize(self) -> list[token]:
        result: list[token] = []
        while 0 < len(self.code):
            for i in self.rules:
                mo = re.match(self.rules[i], self.code)
                if mo:
                    if i != "skip" and i != "ignore":
                        result.append(token(i, mo.group(1)))
                        self.reline(mo.group(0))
                        break
                    else:
                        self.reline(mo.group(0))
                        break
            else:
                raise wrong_token_error()

        return result
