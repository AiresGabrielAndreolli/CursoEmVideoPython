def linha(carac, tam):
    print(carac*tam)
def escreva(texto):
    linha('~', len(texto)+4)
    print(texto)
    linha('~', len(texto)+4)


escreva('  Curso de Python')
escreva('  GABRIEL')