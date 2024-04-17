'''Ex05 - Verificador de Palíndromos: Solicite ao usuário que 
digite uma palavraou frase e verifique se é um palíndromo 
(ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).'''

palavra = input("Digite a palavra a ser verificada: ")
def retorna_ultimas_letra(palavra):
    return palavra[::-1]

if palavra == retorna_ultimas_letra(palavra):
    print("É um palindromo")
else:
    print("Não é um palindromo")