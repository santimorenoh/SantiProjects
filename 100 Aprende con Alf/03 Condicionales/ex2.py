user_password = 'est'

entered_password = input('Ingrese la contraseña: ')

if entered_password.lower() == user_password.lower():
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')
