n = int(input("Digite a quantidade de numeros: "))
cont = 1

penNum = 0
ultNum = 1
numAtual = 1

while cont <= n:
    if n == 1:
        print(penNum)
    if n == 2:
        print(ultNum)
    else:
        print(numAtual)
        
        numAtual = penNum + ultNum
        penNum = ultNum
        ultNum = numAtual
    cont += 1
