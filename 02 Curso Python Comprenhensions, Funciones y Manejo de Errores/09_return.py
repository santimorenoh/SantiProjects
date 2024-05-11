def find_volume(lenght = 1, width = 1, depth = 1):
    return lenght * width * depth, width, 'Hola'

result, width, text = find_volume(width = 10)

print(result)
print(width)
print(text)