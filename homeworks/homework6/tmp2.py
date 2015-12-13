
#rosalind (conditions and loops -- считаем сумму всех нечентных чисел от а до б)
# a = int(input())
# b = int(input())
# sum = 0
# while a <= b:
#     if a%2 != 0:
#         sum +=  + a
#         a += 2
#     else:
#         a += 1
# print(sum)

#rosalind(file works = выводим нечетные строки)input_file = open('test.txt', 'r')
# sentences = input_file.read().split('\n')
# out1 = open('file2.txt', 'w')
# out2 = open('file3.txt', 'w')
# for index, data in enumerate(sentences):
#     if index % 2 != 0:
#         print(data, sep = '\n')
#     else:
#         out2.write(data)
# input_file.close()
# out1.close()
# out2.close()


#rosalind(dictionary)
import sys
import os
import re

# читаем файл
# file = open("rosalind_ini6.txt",'r')
# try:
#     txt = file.read()
# finally:
#     file.close()

# выбираем слова через регулярные выражения
# p = re.compile("([a-zA-Z-']+)")
# res=p.findall(txt)


# создаем словарь. Ключ-слово, Значение-частота повторения
# lsWord = {}
# for key in res:
   # key = key.lower()
   #  if key in lsWord:
   #      value = lsWord[key]
   #      lsWord[key]=value+1
   #  else:
   #      lsWord[key]=1

# создаем список ключей отсортированный по значению словаря lsWord
# for key, value in lsWord.items():
#     print(key, value)

#можем сортировать
# b = str(lsWord)
# b.sort
# for key in b:
# print(key +' '+ str(dct[key]))


#rosalind()

a = "GCTATAAA"
dct = {}
for key in a:
    if key in dct:
        value = dct[key]
        dct[key] = value+1
    else:
         dct[key]=1
b = list(dct.keys())
b.sort()
for key in b:
    print(dct[key],end = ' ')


