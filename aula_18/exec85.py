numeros = [[], []]

# numeros[0] -> par
# numeros[1] -> impar

for i in range(0, 7):
    num = int(input("Digite um número: "))
    numeros[num % 2].append(num)

numeros[0].sort()
numeros[1].sort()

print(f'Os números pares são {numeros[0]}')
print(f'Os números impares são {numeros[1]}')