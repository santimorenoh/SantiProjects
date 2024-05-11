age = int(input('Ingrese su edad: '))
anual_earns = float(input('Digite sus ingresos mensuales: '))

if age > 16 and anual_earns >= 1000:
    print('Usted debe tributar')
else:
    print('Usted no debe tributar')