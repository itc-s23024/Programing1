def outer(a, b):
    print("outer function(a,b) = ({}, {})".format(a, b))

    def inner(c, d):
        print("inner function (c, d) = ({}, {})".format(c, d))
        return c * d

    return inner(a, b)


a = outer(4, 7)
print(a)
