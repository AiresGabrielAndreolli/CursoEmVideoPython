qtdTermo = int(input("Digite a quantidade de termos: "))
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

i = 0

while i < qtdTermo:
    print(termo)
    termo += razao
    i += 1