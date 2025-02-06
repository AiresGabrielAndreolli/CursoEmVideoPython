soma = 0
qtdNum = 0

while True:
    n = int(input("Digite o num (Para sair use 999): "))
    if n == 999:
        break
    soma += n
    qtdNum += 1
print(f"A quantidade de numeros digitados foi {qtdNum}\nA soma foi {soma}")