with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)

    file.write('Nuevas cosas en este archivo\n')
    file.write('una linea\n')
    file.write('otra mas\n')
    file.write('otra mas\n')