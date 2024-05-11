person = {
  'name': 'Nico',
  'last_name': 'Molina',
  'langs': ['Python', 'JavaScript'],
  'age': 99
}

print(person)

person['prueba'] =  'prueba'
print(person)

person['name'] = 'Santi'
person['age'] -= 50
person['langs'].append('Rust')
print(person)

del person['last_name']
person.pop('age')

print(person)


print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
