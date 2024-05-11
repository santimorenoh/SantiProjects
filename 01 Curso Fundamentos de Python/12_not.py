print(not True)
print(not False)

print("NOT AND")
print("True NOT AND True = ", not (True and True))
print("True NOT AND False = ", not (True and False))
print("False NOT AND True = ", not (False and True))
print("False NOT AND False = ", not (False and False))

stock = input("Ingrese el numero de stock => ")
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))