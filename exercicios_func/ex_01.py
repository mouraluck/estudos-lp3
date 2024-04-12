''' Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente.
 Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.'''

 
import random


num = random.randint(1,100)

def retorna_se_maior(ent,num):
    if ent >100 or ent <1:
        return f'fora da faixa'
    elif ent > num:
        return f'Tá alto fio'
    elif ent < num:
        return f'Ta baixo fio'
    elif ent == num:
        print("Acertou miseravi")
        

while True:
    ent = int(input())
    
    print(retorna_se_maior(ent= ent, num= num))
    if ent == num:
        break
    