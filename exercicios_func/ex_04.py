'''Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos.
O programa deve pedir ao usuário para votar várias vezes e, no final,
mostrar o número de votos de cada candidato e quem foi o vencedor.'''
v1= 0
v2= 0
v3 = 0
while True:
    voto = int(input("Votar no candidato 1: 1 \nVotar no Candidado 2: 2\nVotar no candidato 3: 3\nEncerrar votação: 0\n"))
    if voto == 0:
        break
    elif voto == 1:
        v1 +=1
    elif voto == 2:
        v2 +=1
    elif voto == 3:
        v3 +=1
    else: 
        print("opção inválida")

print(f"O candidato 1 teve {v1} votos\nO candidato 2 teve {v2} votos\nO candidato 3 teve {v3} votos")