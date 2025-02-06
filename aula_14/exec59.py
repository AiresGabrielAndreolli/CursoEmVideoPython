opc = 0
result = 0
a = b = 0
while opc != 5:
    print('''[1] Somar
[2] Multiplicar
[3] maior
[4] novos numeros
[5] sair''')
    opc = int(input("Digite a opção: "))
    print()
    match opc:
        case 1:
            result = a + b
            print("A soma é {}".format(result))
        case 2:
            result = a * b
            print("O fator é {}".format(result))
        case 3:
            result = a if a > b else b
            print("O maior é {}".format(result))
        case 4:
            a = int(input("Digite o novo a: "))
            b = int(input("Digite o novo b: "))
        case 5:
            print("Saindo")
            #n faz nd
        case _:
            print("Opção inválida!")
