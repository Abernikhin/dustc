from lexer.lexer import lexer, token


def lexical_analiz(source: str) -> list[token]:
    l: lexer = lexer(source)
    return l.tokenize()

