import sys
print(sys.path)

import re
texto = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es el 13'
result = re.findall('[0-9]+', texto)
print(result)


import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)


import collections
numbers = [1, 1, 2, 3, 4, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4]
counter = collections.Counter(numbers)
print(counter)