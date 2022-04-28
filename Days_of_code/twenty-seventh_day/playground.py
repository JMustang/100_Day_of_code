

# def foo(*args):
#     for n in args:
#         print(n)


# foo(1, 2, 3, 4, 5)


# def sum(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total


# print(sum(1, 2, 3, 4, 5))
# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)


# bar(1, 2)

# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)


# bar(toast='nah', spam=4, eggs=2)


# def test(*args):
#     print(type(args))


# test(1, 2, 3, 5)

# def test(*args):
#     print(args)


# test(1, 2, 3, 5)

def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
