'''Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca.
O programa começa com uma palavra oculta (o usuário não vê) e o
usuário tenta adivinhar a palavra, letra por letra. O usuário tem
 um número limitado de tentativas para adivinhar toda a palavra.'''

'''
Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. 
O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, 
letra por letra. 
O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
'''
# nao to conseguindo tirara o numero de chances conforme o usuário joga

def forca(palavra):
    
    letras_entrada = []
    chances = 7
    ganhou = False
    
    while True:
        
        for letra in palavra:
            
            if letra.lower() in letras_entrada:
                print(letra, end=" ")

            else:
                print("_", end=" ")

        
        print(f"Você tem {chances} chances")
        tentativa = input("Digite uma letra: ")
        

        letras_entrada.append(tentativa.lower())

        if tentativa.lower() not in palavra.lower():
            chances -= 1

        ganhou = True

        for letra in palavra:
            
            if letra.lower() not in letras_entrada:
                ganhou = False

        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f"Ganhou! Parabens a palavra é {palavra}")

    else:
        print(f"Ja eraaa, a palavra correta era: {palavra}")


palavra = input('Digite a palavra a ser adivinhada')
forca(palavra)