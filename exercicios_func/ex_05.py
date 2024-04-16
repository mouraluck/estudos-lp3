'''Ex05 - Verificador de Palíndromos: Solicite ao usuário que 
digite uma palavraou frase e verifique se é um palíndromo 
(ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).'''

palavra = input()
def retorna_ultimas_letra(palavra,letra):
    return palavra[::-1][:palavra.index(letra) + 1:]

for letra in palavra:
    print(letra, retorna_ultimas_letra(palavra, letra)) 