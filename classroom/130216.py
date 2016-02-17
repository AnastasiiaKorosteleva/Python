__author__ = 'anastasiiakorosteleva'
# one
# import traceback
#
# def a(i):
#     b(i - 1)
#
# def b(i):
#     if i > 0:
#         a(i - 1)
#     else:
#         traceback.print_stack()
#
# #two
# try:
#     15/0
# except ZeroDivisionError:
#     print("It's alive, Alive")
#
# def f(x):
#     try:
#         return 15 / x
#     except TypeError:
#         print("Type error =(")
#     except ZeroDivisionError:
#         print("Whaaaat")
# print(f(4))
# print(f(0))
# f(0)
# f([])
#
# #three
# def f(x):
#     try:
#         return 15 / x
#     except (TypeError, ZeroDivisionError):
#         print("Whaaaat")
# print(f(4))
# print(f(0))
# f(0)
# f([])
#
# #four
#
# def f(x):
#     try:
#         return 15 / x
#     except (TypeError, ZeroDivisionError) as err:
#         print(type(err))
#         print(err)
#         print(err.args)
# print(f(4))
# print(f(0))
# f(0)
# f([])

#five

# try:
#     x = open("test.txt", "r")
# except FileNotFoundError:
#     print("BAAAAAAD")
# else:
#     data = x.read()
#     print(data)
#     x.close()

#sixth

# def divide(x, y):
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         print("Div by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finnaly close")
#
#
# divide(15, 4)

#seven

#
# def append(x, el):
#     if not type(x) is list:
#         raise TypeError("First arg should be a list")
#     else:
#         x.append(el)
# try:
#     append(6, 5)
# except TypeError:
#     print("TypeError")




#eight

class RangeIterator:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.j:
            ret_val = self.i
            self.i += 1
            return ret_val
        else:
            raise StopIteration("No more el")

it = RangeIterator(10, 11)
for x in it:
    print(x)