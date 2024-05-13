score = float(input('Ingrese la puntuación del empleado: '))
amount  = 2400

if score == 0:
    performance = 'Inaceptable'
    amount = score * amount
elif score == 0.4:
    performance = 'Aceptable'
    amount = score * amount
elif score >= 0.6:
    performance = 'Meritorio'
    amount = score * amount

print(f'Su nivel de rendimiento es {performance} y recibirá ${amount}')
