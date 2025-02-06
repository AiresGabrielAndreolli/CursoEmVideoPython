def area(l, c):
    print(f'A area de um terreno {l:.1f}x{c:.1f} é {l*c:.1f}m²')


print(' Controle de terrenos')
print('-'*30)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)