totalCompra = qtdProdMaiorMil = cont = 0
while True:

    nomeProd = str(input("Nome do produto: "))
    precoProd = float(input("Preço do produto: "))

    if precoProd > 1000:
        qtdProdMaiorMil += 1

    totalCompra += precoProd

    if not(cont) or precoProd < precoMaisBarato:
        nomeMaisBarato = nomeProd
        precoMaisBarato = precoProd

    cont += 1

    while True:
        continuar = str(input("Continuar? (S/N) "))
        if continuar in 'NnSs':
            break
    if continuar in 'Nn':
        break

print(f'Mais que mil {qtdProdMaiorMil}  Total R${totalCompra:.2f}  Prod Mais barato {nomeMaisBarato}')