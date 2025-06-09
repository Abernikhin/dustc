from parser.parser import parser, token, node


def build_ast(tokens: list[token]) -> list[node]:
    p = parser(tokens)
    return p.parsing()
