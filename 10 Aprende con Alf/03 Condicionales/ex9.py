age = int(input('Ingrese la edad: '))

if age < 4:
    print('Entra gratis')
elif age <= 18:
    print('Debe pagar 5 euros')
else:
    print('Debe pagar 10 euros')