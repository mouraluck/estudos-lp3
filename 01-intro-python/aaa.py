
import math
'''n1 = int(input())
n2 = int(input())
r = n1+n2
print("X = {}".format(r))

N = 3.14159
raio = float(input())

area = raio*raio*N

print("A={:.4f}".format(area))

n1 = float(input())
n2 = float(input())
soma = (n1*3.5)+(7.5*n2)
MEDIA = soma/11
print("MEDIA = {:.5f}".format(MEDIA))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

solutionX = (x2 - x1)
solutionY = (y2 - y1)
dab = math.sqrt((solutionY** 2) + (solutionX** 2))
print("{:.4f}".format(dab))'''

'''
Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. 
O programa deve pedir ao usuário para votar várias vezes e, no final, 
mostrar o número de votos de cada candidato e quem foi o vencedor.
'''

candidato_1 = 0 # lala
candidato_2 = 0 # momota
candidato_3 = 0 # querido

def adciona_voto(voto, candidato_1,candidato_2,candidato_3):
    if (voto == 1):
        print ('você votou no Latorre')
        candidato_1 = candidato_1 +1
    elif (voto == 2):
        print ('você votou no Motta')
        candidato_2 = candidato_2 +1
    else:
        print ('você votou no Quirino')
        candidato_3 = candidato_3 +1

def votacao(candidato_1, candidato_2, candidato_3):
    contador = 0
    while (contador < 3):
        print('Em quem você deseja votar?')
        voto = int(input('1 - Latorre || 2 - Motta || 3 - Quirino '))
        print()
        adciona_voto(voto,candidato_1,candidato_2,candidato_3)
        if voto in [1,2,3]:
        #if(voto == 1 or voto == 2 or voto == 3):
            contador = contador + 1

def contagem(candidato_1, candidato_2, candidato_3):
    if max(candidato_1,candidato_2,candidato_3) == candidato_1:
        return 'Latorre ganhou!'

    elif max(candidato_1,candidato_2,candidato_3) == candidato_2:
        return('Motta ganhou!')

    elif max(candidato_1,candidato_2,candidato_3) == candidato_3:
        return('Quirino ganhou!')

    else:
        print('Ocorreu um empate, vote novamente!')
        votacao(candidato_1, candidato_2, candidato_3)
        contagem(candidato_1, candidato_2, candidato_3)

        # vai direto pro else, mesmo que não ocorra empate


votacao (candidato_1, candidato_2, candidato_3)
print ('Votação encerrada, vamos as apurações')
print(contagem(candidato_1, candidato_2, candidato_3))