valAux = valSacado = int(input("Valor a ser sacado: R$"))

qtdUm = qtdDez = qtdVinte = qtdCinq = 0

while True:
    if valSacado == 0:
        break
    if valSacado >= 50:
        qtdCinq += 1
        valSacado -= 50
    elif valSacado >= 20:
        qtdVinte += 1
        valSacado -= 20
    elif valSacado >= 10:
        qtdDez += 1
        valSacado -= 10
    else:
        qtdUm += 1
        valSacado -= 1

print(f'Você pode sacar R${(qtdCinq*50) + (qtdDez*10) + (qtdVinte*20) + (qtdUm)} com {qtdCinq} notas de R$50, {qtdVinte} notas de R$20, {qtdDez} notas de R$10 e {qtdUm} notas de R$1')