__author__ = 'anastasiiakorosteleva'

input_file = open('yazkora.txt', 'r')
sentences = input_file.read().split('.')

file = open("answer.txt", 'w')

for sentence in sentences:
    words = sentence.split()
    list_of_words = []
    for word in words:
        if word[len(word) - 2:] == 'yo':
            list_of_words.append(word)
    str = (' '.join(list_of_words))
    file.write(str + '\n')

input_file.close()
file.close()