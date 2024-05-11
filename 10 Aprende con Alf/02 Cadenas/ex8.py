price = input('Ingrese el precio del producto en euros con dos decimales: ')

print('Euros: ' + price[:price.find('.')] + '  Céntimos: ' + price[price.find('.') + 1:])

