# Solicita ao usuário seu peso e altura
peso = float(input("Entre com o peso (Kg): "))
altura = float(input("Entre com a altura (m): "))

# Função para calcular o IMC
def calcula_imc(peso, altura):
    return peso / (altura * altura)

# Função para verificar a classificação do IMC
def verifica_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc >= 18.5 and imc <= 24.9:
        return "Peso normal"
    elif imc >= 25.0 and imc <= 29.9:
        return "Excesso de peso"
    elif imc >= 30.0 and imc <= 34.9:
        return "Obesidade de Classe 1"
    elif imc >= 35.0 and imc <= 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

# Função para calcular o peso a ser ganho ou perdido para atingir o peso normal
def peso_ideal(peso, altura):
    peso_normal_superior = 24.9 * (altura * altura)
    if peso > peso_normal_superior:
        return f"Você precisa perder {peso - peso_normal_superior:.2f} Kg para atingir o peso normal."
    else:
        return "Você está dentro do peso normal."

# Calcula o IMC
imc = calcula_imc(peso, altura)

# Imprime o IMC e a classificação
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {verifica_imc(imc)}")

# Imprime quanto peso precisa ser ganho ou perdido para atingir o peso normal
print(peso_ideal(peso, altura))
