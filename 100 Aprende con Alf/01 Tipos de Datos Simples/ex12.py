bread_full_price = 3.49
discount = 60/100
discounted_bread_qty = int(input('Ingrese la cantidad de barras de pan vendidas que no son del día: '))

print(f'El precio de la barra de pan es de ${bread_full_price}')
print(f'El descuento realizado por pan es de ${round(bread_full_price * discount, 2)}')
print(f'El costo total es de ${round(bread_full_price * (1 - discount) * discounted_bread_qty, 2)}')