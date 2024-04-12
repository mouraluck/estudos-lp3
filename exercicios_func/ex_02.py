# Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.
tab = int(input("Entre com o numero que dseja ver a tabuada"))

def mostra_tabuada(tab):
    for n in range(10):
        r = (n+1)*tab
        print(f"{tab} x {n+1} = {r}")

mostra_tabuada(tab)