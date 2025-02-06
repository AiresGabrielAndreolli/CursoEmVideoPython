from random import randint

qtdVit = 0

while True:
    escolhaJog = int(input("Digite Par ou impar (0 ou 1): "))
    qtdDedosJog = int(input("Digite a quantidade de dedos: "))

    qtdDedosPc = randint(0, 10)

    soma = qtdDedosJog + qtdDedosPc
    print(f'A soma dos dedos é {soma}')
    
    result = soma % 2

    if escolhaJog != result:
        break
    
    qtdVit += 1

print(f'Você ganhou {qtdVit} vezes seguidas')