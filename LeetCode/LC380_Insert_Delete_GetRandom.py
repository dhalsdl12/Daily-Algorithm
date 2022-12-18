import random

class RandomizedSet:
    def __init__(self):
        self.stack = []
        return None

    def insert(self, val: int) -> bool:
        if val in self.stack:
            return False
        self.stack.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.stack:
            return False
        self.stack.remove(val)
        return True

    def getRandom(self) -> int:
        num = randint(0, len(self.stack) - 1)
        return self.stack[num]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()