# subtotal = float(input("Ingresar monto de factura: "))
# propina = float(input("Ingresar % de propina: ")) / 100 * subtotal

# total = subtotal + propina   

# print("Propina: " + str(propina))
# print("Total a pagar: " + str(total))

start = int(input("Rango inicial: "))
end = int(input("Rango final: "))

primes = []

for i in range(start, end + 1):
    
    counter = 0
    
    for j in range(1, i):

        if i % j == 0:
            counter += 1

    if counter < 2:

        primes.append(i)

print("Números primos en el rango dado: " + str(primes))