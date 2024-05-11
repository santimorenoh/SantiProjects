print("AND")
print("True AND True = ", True and True)
print("True AND False = ", True and False)
print("False AND True = ", False and True)
print("False AND False = ", False and False)

print("*" * 50)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = input("Ingrese el numero de stock => ")
stock = int(stock)

print(stock >= 100 and stock <= 1000)

print("OR")
print("True OR True = ", True or True)
print("False OR True = ", True or False)
print("True OR False = ", False or True)
print("False OR True = ", False or False)

role = input("Digita tu rol -> ")
print(role == "admin" or role == "seller")