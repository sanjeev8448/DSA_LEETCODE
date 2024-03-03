class StockSpanner:
    def __init__(self):
        self.stack = []  # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        # print(self.stack)
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]

            # print(span)
            self.stack.pop()
            print(self.stack)
        self.stack.append((price, span))
        return span
s = StockSpanner()
a = s.next(100)
a1 = s.next(80)
a2 = s.next(60)
a3 = s.next(70)
a4 = s.next(60)
a5 = s.next(75)
a6 = s.next(85)
print("ok")
print(a)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)

 