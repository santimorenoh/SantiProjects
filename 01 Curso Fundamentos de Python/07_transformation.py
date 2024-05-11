name = "Santiago"
print(type(name))

name = 12
print(type(name))

name = True
print(type(name))


print("Santiago" + "Moreno")
print(10 + 20)
#No se puede print("Santiago" + 10)
print("Santiago" + "27")

age = 29

print("Mi edad es " + str(age))
print(f"Mi edad es {age}")


age = input("Digite su edad -> ")
print(type(age))
age = int(age)
print(f"Tu edad en 10 años será {age + 10}")