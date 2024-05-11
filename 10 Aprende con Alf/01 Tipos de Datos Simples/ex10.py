clown_weight = 112
doll_weight = 75

clowns_number = int(input('Ingresar el número de payasos: '))
dolls_number = int(input('Ingresar el número de muñecas: '))

total_weight = clowns_number * clown_weight + dolls_number * doll_weight

print(f'El peso total del paquete que será enviado es de {total_weight} kg')