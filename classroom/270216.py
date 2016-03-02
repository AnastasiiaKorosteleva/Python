__author__ = 'anastasiiakorosteleva'
#lambda
# x = lambda x,a: x+a
# print((lambda x,a: x+a)(1,2))
# numbers = input().split(" ")
# numbers = map(int, numbers)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

#пишем map
# class Map:
#     def __init__(self, f, iterable):
#         self.f = f
#         self.it = iter(iterable)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return self.f(next(self.it))
# for i in Map(int, ["12", "13", "14"]):
#     print(i)

# x = Map(int, ["12", "13", "14"])
#
# print(next(x.it))
# print(next(x.it))
# print(next(x.it))
# try:
#
# except:
#
# for i in Map(int,["12", "13", "14"]):
#     print(i)

# def my_map(f, iterable):
#     for element in iterable:
#         yield f(element)
# #
# # for i in my_map(int,["12", "13", "14"]):
# #     print(i)
#
# x = my_map(int, ["12", "13", "14"])
# print(next(x))
# print(next(x))
# print(next(x))


# lst = [1,2,3,4,5,6,7,8,9,10]
# y = list(filter(lambda x: x%2 == 0, lst))
# print(y)

# a, b, c = list(map(int, input().split(" ")))
# print(a, b, c)


a, b, *c, d, e, f = "skljdskjsld"
print(a, b)
print(d, e, f)
print(c)

a,b, *c, {"a":12, "b":13, "c":14}