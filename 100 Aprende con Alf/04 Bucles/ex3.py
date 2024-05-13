num = int(input("Inserte un número entero positivo: "))

for i in range(num):
  if (i + 1) % 2 == 1:
    print((i + 1), end = ', ')
