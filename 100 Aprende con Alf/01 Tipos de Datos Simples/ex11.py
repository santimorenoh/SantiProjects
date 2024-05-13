initial_amount = float(input('Ingrese cantidad de dinero depositada: '))

anual_rate = 4/100

final_value = initial_amount

for i in range(3):
    final_value = final_value + final_value * anual_rate
    print(f'El valor final de ahorros en el año {i + 1} será de {round(final_value, 2)}')