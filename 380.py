from random import choice


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False

        self.dict[val] = len(self.list)
        self.list.append(val)
        # print(self.dict)
        # print(self.list)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        idx, last_element = self.dict[val], self.list[-1]
        print(idx)
        # print(last_element)
        self.list[idx], self.dict[last_element] = last_element, idx
        self.list.pop()
        del self.dict[val]
        # print(self.dict)
        # print(self.list)

        return True

    def getRandom(self) -> int:
        return choice(self.list)
    
    
    
s =  RandomizedSet()
a = s.insert(1)
# print(a)
# b = s.remove(2)
# print(b)
c = s.insert(2)
# print(c)
# d = s.getRandom()
# print(d)
# e = s.remove(1)
# print(e)
# f = s.insert(2)
# print(f)
# g = s.getRandom()
# print(c)

