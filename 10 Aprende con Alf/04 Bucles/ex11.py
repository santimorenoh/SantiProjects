word = input('Ingrese una palabra: ')

for i in range(len(word)):
    print(word[len(word) - i - 1], end = ' ')