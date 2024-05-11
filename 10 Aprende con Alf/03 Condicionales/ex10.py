vegetarian = input('Ingrese si desea pizza vegetariana o no: ')

if vegetarian == 'si':
    print('Menú de ingredientes:')
    print('- Pimiento')
    print('- Tofu')
else:
    print('Menú de ingredientes:')
    print('- Peperoni')
    print('- Jamon')
    print('- Salmón')

selected_ingredient = input('Elija uno: ')

print(f'Su pizza {vegetarian} es vegetariana y los ingredientes son Mozzarella, Tomate y {selected_ingredient}')