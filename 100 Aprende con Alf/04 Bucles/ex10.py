num = int(input('Ingrese un numero: '))

is_prime = True
counter = 0

for i in range(num):
  if num % (i + 1) == 0:
    counter = counter + 1

if counter > 2:
  print(f"El número {num} no es un número primo")
else:
  print(f"El número {num} es un número primo")