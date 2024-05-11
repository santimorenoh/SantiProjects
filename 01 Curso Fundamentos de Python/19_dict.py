my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': 'bla bla bla',
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))
print(my_dict.get('valor_que_no_existe'))

# con el get me retorna un valor que se puede manejar en ejecución, mientras que
# si pregunto con [] y esa key no existe, arroja eeror el programa y se detiene la
# ejecución

print('avion' in my_dict)
print('carro' in my_dict)
