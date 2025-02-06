palavra = str(input("Digite uma palavra: ")).strip().upper()
junto = ''.join(palavra)
inverso= ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print("É")
else:
    print("não e")