memory = []


class var():
    def __init__(self) -> None:
        memory.append(0)
        self.lit = len(memory)-1

    def set(self, obj) -> None:
        memory[self.lit] = obj

    def get(self):
        return memory[self.lit]


nums = var()
for i in range(10):
    memory.append(0)
num = var()
num2 = var()
memory[nums.lit+1] = num.lit
memory[nums.lit+2] = num2.lit

print("dump[0]")
