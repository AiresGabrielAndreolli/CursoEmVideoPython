isPalin = True
palavra = str(input("Digite uma palavra: "))
palavra = palavra.strip()
meio = int(len(palavra)/2)
palavra = palavra.upper()
for i in range(0, meio):
    if palavra[i] != palavra[len(palavra) - i - 1]:
        isPalin = False
print(isPalin)