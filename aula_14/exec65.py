permanecer = 'S'
cont = 0
soma = 0

while permanecer == 'S':
    
    num = int(input("Digite o numero: "))

    soma += num

    # Começo da verificação do maior e do menor

    if not(cont):
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    
    # Fim da verificação do maior e do menor

    permanecer = str(input("Continuar? (S/N) "))

    cont += 1

media = soma/cont

print("O maior número é {}  O menor número é {}".format(maior, menor))
print("A média é {}".format(media))