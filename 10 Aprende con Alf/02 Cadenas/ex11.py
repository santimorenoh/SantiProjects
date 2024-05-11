product = input('Ingrese el nombre del producto: ')
price = float(input('Ingrese el precio del producto: '))
qty = int(input('Ingrese la cantidad del producto: '))


print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = product, unidades = qty, precio = price, total = qty * price))
