from ganare.ganare import ganare


def gc(ast, char) -> str:
    g = ganare(ast)
    return g(char)
