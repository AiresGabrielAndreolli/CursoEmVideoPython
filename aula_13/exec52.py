isPrimo = True
num = int(input("Digite um numero: "))
for i in range(num - 1, 1, -1):
    if not(num%i):
        isPrimo = False
print(isPrimo)