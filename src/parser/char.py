class symantic_not_find_name_error(Exception):
    pass


class symantic_type_error(Exception):
    pass


class char():
    def __init__(self) -> None:
        self.type = ["number"]
        self.name = []
        self.func = []

    def add_type(self, type: str) -> None:
        self.type.append(type)

    def get_type(self, type) -> bool:
        if type in self.type:
            return True
        return False

    def add_name(self, name: str, _type: str) -> None:
        self.name.append({"name": name, "type": _type})

    def add_func(self, type: tuple) -> None:
        self.func.append(type)

    def get_func(self, func_name: str) -> bool:
        for i in self.name:
            if i[0] == func_name:
                return True
        return False

    def get_args_func(self, *args) -> bool:
        for i in self.func:
            for a in range(1, len(i)):
                if a == args:
                    return True
        return False

    def gname(self, name) -> dict:
        for i in self.name:
            if i["name"] == name:
                return i
        raise symantic_not_find_name()

    def get_name(self, name) -> bool:
        for i in self.name:
            if i["name"] == name:
                return True
        return False
