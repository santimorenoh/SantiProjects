equity = float(input('Ingrese cantidad a invertir: '))

interest = float(input('Ingrese porcentaje (%) de interés anual: '))

years = int(input('Ingrese cantidad de años: '))

for i in range(years):
  equity = equity + equity * interest/100
  print(f'El capital obtenido correspondiente al año {i + 1} es de {equity}')