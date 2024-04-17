'''
Ex08 - Função de Contagem de Palavras: Escreva uma função que receba 
uma string (frase) como argumento e retorne um dicionário onde as 
chaves são as palavras únicas no texto e os valores são o número de 
vezes que cada palavra aparece no texto. Depois, teste a função com 
diferentes textos fornecidos pelo usuário.
'''

def contar_palavras(frase):
    cont = {}
    palavras = frase.split()

    for palavra in palavras:
        if palavra in cont:
            cont[palavra] += 1
        else:
            cont[palavra] = 1

    return cont

frase = input("Digite uma frase: ")
resultado = contar_palavras(frase)

print("Contagem de palavras:")
print(contar_palavras(frase))