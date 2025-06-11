from lexer import lexical_analiz
from parser import build_ast
from ganare import gc


def main() -> int:
    with open(input("&> "), 'r')as f:
        source = f.read()
    tokens = lexical_analiz(source)
    # for i in tokens:
    #     i.info()
    ast = build_ast(tokens)[0]
    char = build_ast(tokens)[1]
    # for i in ast:  # type: ignore
    #     i.info()
    with open('out.py', 'w')as f:
        f.write(gc(ast, char))  # type: ignore

    return 0


print(f"\ndump[{main()}]")
