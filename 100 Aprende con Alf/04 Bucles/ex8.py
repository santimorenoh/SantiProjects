num = int(input('Ingrese un número entero: '))

for i in range(1, num + 1, 2):
  for j in range(1, i + 1, 2):
    # if (i - j) % 2 != 0:
    print((i + 1 - j), end = '\t')
  print('')
    