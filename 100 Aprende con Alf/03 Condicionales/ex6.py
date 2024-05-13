name = input('Ingrese su nombre: ')
sex = input('Ingrese su sexo (M para Masculino y F para Femenino): ')

if (sex == 'F' and name[0] < 'M') or (sex == 'M' and name[0] > 'N'):
    print('Pertenece al grupo A')
else:
    print('Pertenece al grupo B')


