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
                    elif i.child[0].type == "arr name":
                        self.reslut += f"{i.child[0].lit} = var()\n"
                        self.reslut += f"for i in range({i.child[0].child[0].lit}):\n"
                        self.reslut += "    memory.append(0)"
                elif i.type == "eq":
                    self.reslut += self.math(i.child[0]) + ' = ' + self.math(i.child[1]) # type: ignore
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
            if branch.child[0].ltype == "operator&":
                r = f"{branch.child[0].child[0].lit}.lit"
            elif branch.type == "index":
                r = f"memory[{branch.child[0].lit}.lit+{branch.lit}]"
            if branch.child[0].ltype == "name":
                r = f"memory[{branch.child[0].lit}.lit]"
            else:
                r += branch.child[0].lit
            r += branch.lit
            r += self.math(branch.child[1])
            return r
        if branch.type == "incr":
            return "+ 1"
        if branch.type == "decr":
            return "- 1"
        if branch.type == "call":
            r = branch.lit + '('
            for i in branch.child:
                r += self.math(i)+', '
            r += ')'
            return r
        elif branch.type == "op":
            if branch.ltype == "operator&":
                return f"{branch.child[0].lit}.lit"
            elif branch.ltype == "index":
                return f"memory[{branch.child[0].lit}.lit+{branch.lit}]"
            elif branch.ltype == "name":
                if branch.child.__len__() != 0:
                    return f"memory[{branch.lit}.lit] {self.math(branch.child[0])}"
                return f"memory[{branch.lit}.lit]"
            return branch.lit

        return ''
