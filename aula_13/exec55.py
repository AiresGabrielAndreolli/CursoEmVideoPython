for i in range(0, 5):
    
    num = float(input("Digite o peso: "))

    if not(i):
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print("Maior: {:.2f}\nMenor: {:.2f}".format(maior, menor))
