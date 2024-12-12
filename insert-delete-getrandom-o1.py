import random


class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.list.append(val)
            self.set[val] = len(self.list) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            index = self.set[val]
            if index < len(self.list) - 1:
                self.list[index] = self.list[-1]
                self.set[self.list[index]] = index
            self.list.pop()
            del self.set[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list) - 1)]


s = RandomizedSet()
s.insert(0)
s.insert(1)
s.remove(0)
s.insert(2)
s.remove(1)
print(s.list)
exit(0)

obj = RandomizedSet()
[obj.insert(x) for x in range(10)]
print(obj.remove(20))
print(obj.remove(9))
for i in range(20):
    print(obj.getRandom())
