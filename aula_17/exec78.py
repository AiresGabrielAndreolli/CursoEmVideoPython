valores = [int(input("Digite um número: ")), 
           int(input("Digite um número: ")), 
           int(input("Digite um número: ")), 
           int(input("Digite um número: ")), 
           int(input("Digite um número: "))]

maior = max(valores)
menor = min(valores)

print(f'O maior é {maior} e esta na posição {valores.index(maior)}')
print(f'O menor é {menor} e está na posição {valores.index(menor)}')