n = 0
soma = 0
qtdNum = 0

while n != 999:
    n = int(input("Digite o num (Para sair use 999): "))
    soma += n
    qtdNum += 1
soma -= 999
qtdNum -= 1
print("A quantidade de numeros digitados foi {}\nA soma foi {}".format(qtdNum, soma))