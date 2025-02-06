palavras = ('Feijao', 'arroz', 'lasanha', 'marmelada')
vogais = ('A', 'E', 'I', 'O', 'U')

for pos, palavra in enumerate(palavras):
    print(f'A palavra {palavra} tem', end=' ')
    for i, vogal in enumerate(vogais):
        if vogal in palavra.upper():
            print(f'a vogal {vogal}', end=' ')
    print('\n__________________________\n')

for pos, palavra in enumerate(palavras):
    print(f'A palavra {palavra} tem', end=' ')
    for i, letra in enumerate(palavra):
        if letra.upper() in vogais:
            print(f'{letra}', end=' ')
    print('\n__________________________\n')