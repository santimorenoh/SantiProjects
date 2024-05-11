set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries) # 'col' está en ese conjunto?
print('pe' in set_countries) # 'pe' está en ese conjunto?

# add

set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)


# remove
set_countries.remove('col')
print(set_countries)

set_countries.remove('ar')
print(set_countries)

set_countries.discard('arg') # No falla el programa si no existe. Con remove si falla
print(set_countries)

set_countries.add('arg')
print(set_countries)

set_countries.clear()
print(set_countries)
print(len(set_countries))
