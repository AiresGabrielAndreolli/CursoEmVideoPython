numPorExt = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input("Digite um número entre (0 e 20): "))
    if n in range(0, 21):
        break
    print("Tente novamente! ", end='')
print(numPorExt[n])