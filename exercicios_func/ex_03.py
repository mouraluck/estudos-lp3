# Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.
frase = input("Entre com a frase desejada")
isVogal=False
def conta_letra(l):
    if l in 'AEIOUaeiou':
        return True
    elif l in " .,?!:;/-":
        return None
    else:
        return False

vogais = 0
consoantes = 0

for x in frase:
    if conta_letra(x) == True:
        vogais +=1
    elif conta_letra(x) == None:
        continue
    else:
        consoantes +=1

print(f'{vogais} vogais e {consoantes} consoantes')