numero = int(input("Digite a nota do aluno: "))

def retorna_nota(numero):
    if numero >= 96 and numero > 100:
        return "A+"
    elif numero <= 96 and numero > 93:
        return "A"
    elif numero <= 93 and numero > 90:
        return "A-"
    elif numero <= 90 and numero > 86:
        return "B+"
    elif numero <= 86 and numero > 83:
        return "B"
    elif numero <= 83 and numero > 80:
        return "B-"
    elif numero <= 80 and numero > 76:
        return "C+"
    elif numero <= 76 and numero > 73:
        return "C"
    elif numero <= 73 and numero > 70:
        return "C-"
    elif numero <= 70 and numero > 66:
        return "D+"
    elif numero <= 66 and numero > 63:
        return "D"
    elif numero <= 63 and numero > 60:
        return "D-"
    elif numero < 60:
        return "F"
    else:
        return "Fora da faixa"
    
print(retorna_nota(numero))