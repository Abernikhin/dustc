from lexer import lexical_analiz
from parser import build_ast


def main() -> int:
    with open(input("&> "), 'r')as f:
        source = f.read()
    tokens = lexical_analiz(source)
    # for i in tokens:
    #     i.info()
    ast = build_ast(tokens)
    for i in ast:
        i.info()

    return 0


print(f"\ndump[{main()}]")
