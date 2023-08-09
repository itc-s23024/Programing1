a = (1, 2, 3, 4, 5) + (1, 2, 3, 4, 5)
print(a)


tp1 = (1, 2, 3, 4, 5)
tp2 = (1, 2, 3, 4, 5)
p = [x + y for (x, y) in zip(tp1, tp2)]
print(p)


def tpadd(x, y):
    return x + y


p = list(map(tpadd, tp1, tp2))
print(p)
