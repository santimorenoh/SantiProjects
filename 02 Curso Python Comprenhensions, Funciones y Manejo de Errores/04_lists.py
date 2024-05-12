# ------------ List Comprehension

numbers = []

for element in range(1, 11):
    numbers.append(element * 2)
print(numbers)

numbers2 = [element * 2 for element in range(1, 11)]
print(numbers2)

print('')
print('--------------CON CONDICIONALES--------------')
print('')

numbers = []

for element in range(1, 11):
    if element % 2 == 0:
        numbers.append(element * 2)
print(numbers)

numbers2 = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers2)
