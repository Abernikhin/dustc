from parser.node import node


class ganare:
    def __init__(self, ast: list[node]) -> None:
        self.ast = ast
        f = open("./src/ganare/stdlib.py", 'r')
        self.reslut = f.read()+"\n\n"
        f.close()

    def __call__(self, char) -> str:
        for i in self.ast:
            try:
                if i.type == "var type":
                    if i.child[0].type == "var name":  # type: ignore
                        self.reslut += f"{i.child[0].lit} = var()"  # type: ignore
                    elif i.child[0].type == "func name":  # type: ignore
                        r = f"\n\ndef {i.child[0].lit}(\n"
                        for i in i.child[0].child:
                            r += "  "+i.lit+',\n'
                        r += '): ...\n\n'
                        self.reslut += r
                elif i.type == "eq":
                    self.reslut += f"{i.child[0].lit}.set({self.math(i.child[1])})"  # type: ignore
                elif i.type == "call":
                    r = i.lit + '('
                    for i in i.child:
                        r += self.math(i)+', '
                    r += ')\n\n'
                    self.reslut += r
                elif i.type == "new":
                    self.reslut += '\n'
            except IndexError:
                continue

        return self.reslut+"\nprint(\"dump[0]\")\n"

    def math(self, branch: node) -> str:
        if branch.type == "func":
            r = ''
            if branch.child[0].ltype == "name":
                r = f"{branch.child[0].lit}.get()"
            if branch.child[0].ltype == "operator&":
                r = f"memory[{branch.child[0].child[0].lit}.lit]"
            else:
                r += branch.child[0].lit
            r += branch.lit
            r += self.math(branch.child[1])
            return r
        if branch.type == "call":
                r = branch.lit + '('
                for i in branch.child:
                    r += self.math(i)+', '
                r += ')'
                return r
        elif branch.type == "op":
            if branch.ltype == "name":
                return f"{branch.lit}.get()"
            elif branch.ltype == "operator&":
                return f"memory[{branch.child[0].lit}.lit]"
            return branch.lit

        return ''
