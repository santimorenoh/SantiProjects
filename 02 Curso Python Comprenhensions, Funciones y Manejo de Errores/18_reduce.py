import functools

def accum(counter, item):
    
    print('counter ' + str(counter))
    print('item ' + str(item))
    
    return counter + item


numbers = [1, 2, 3, 4]

result = functools.reduce(accum, numbers)

print(result)