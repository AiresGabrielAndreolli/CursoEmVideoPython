from datetime import date

ano = date.today()
ano = ano.year
maior = 0
for i in range(0, 7):
    nasc = int(input("Digite o ano de nascimento: "))
    if ano - nasc >= 21:
        maior += 1
print("Maiores: {}\nMenores: {}".format(maior, 7-maior))