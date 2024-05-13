equity = float(input('Ingrese el monto a invertir: '))
anual_rate = float(input('Ingrese el interés anual: '))
years = int(input('Ingrese ingrese el número de años: '))

fv = round(equity * (1 + anual_rate / 100) ** years, 2)

print(f'El capital obtenido será de {fv}')