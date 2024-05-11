def increment(x):
    return x + 1

increment2 = lambda x: x + 1



def higher_order_func(x, func):
    return x + func(x)

hof2 = lambda x, func: x + func(x)

result = higher_order_func(2, increment)
print(result)

result2 = hof2(2, increment2)
print(result2)

result2 = hof2(2, lambda x: x + 2)
print(result2)

result2 = hof2(2, lambda x: x * 5)
print(result2)