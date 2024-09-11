

def contar_letras_a(texto):

    texto_minusculo = texto.lower()
    
    contagem = texto_minusculo.count('a')

    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

string = input("Informe uma string: ")
resultado = contar_letras_a(string)
print(resultado)