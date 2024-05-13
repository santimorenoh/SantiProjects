weight = float(input('Introduzca su peso en kg: '))

size = float(input('Introduzca su  estatura en metros: '))

body_mass_index = round(weight / size ** 2, 2)

print(f'Tu índice de masa corporal es {body_mass_index}')