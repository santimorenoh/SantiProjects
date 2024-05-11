birthdate = input('Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ')
day = birthdate[:birthdate.find('/')]

birthdate = birthdate[birthdate.find('/') + 1:]

month = birthdate[:birthdate.find('/')]

year = birthdate[birthdate.find('/') + 1:]

print(f'Día {day}, Mes {month}, Año {year}')