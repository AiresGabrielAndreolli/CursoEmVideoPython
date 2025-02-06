num = int(input("Digite um numero: "))
cont = fatorial = num


while cont > 1:
    fatorial *= (cont - 1)
    cont -= 1
print("O fatorial de {} é {}".format(num, fatorial))