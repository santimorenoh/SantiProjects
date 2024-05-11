phrase = input('Inserte una frase: ')

letter = input('Inserte una letra: ')

count = 0

for i in range(len(phrase)):
    if phrase[i] == letter:
        count += 1

print(f'La letra "{letter}" se repite {count} veces')