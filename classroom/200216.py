__author__ = 'anastasiiakorosteleva'

# x = {'a':15, 'b' : 12}
# print(x)
#
class MyDict(dict):
    def __setitem__(self, key, value):
        print("My MASTER CALLED ME")
        return super(MyDict, self).__setitem__(key,value)
        #return dict.__setitem__(self,key, value) (делает то же что и строчка выше)


    def __repr__(self):
        begin = "{\n"
        end = "\n}"
        to_join = [" %s: %s" % (repr(key), repr(self[key]))
                   for key in self]
        return begin + "\n".join(to_join) + end

    def sorted_values(self):
        pairs = self.items()
        pairs = [(pair[1], pair[0]) for pair in pairs] #меняем местами значение и ключ
        pairs = sorted(pairs)   #сортруем по значению по возрастанию
        return [pair[1] for pair in pairs] #выводим ключи соответственно их значению

x = MyDict()
x['a'] = 15
x['b'] = 12
print(x.__repr__())
# print(x)
print(x.sorted_values())


#теперь про exceptions в наследовании
#
# import sys
# sys.exc_info()
#
# class MyException(Exception):
#     pass

# try:
#     raise MyException("I am raising")
# except Exception as e:
#     print("EXCEPT")
#     print(e)
# except MyException as e: #второй раз не заходим в except
#     print(e)


# try:
#     raise 4
# except:
#     type, value, trace = sys.exc_info()
#     print(type)
#     print(value)
#     print(trace)