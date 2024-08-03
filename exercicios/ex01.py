def calcula_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def calcula_potencia(volume, temp_desejada, temp_ambiente):
    return volume * 0.05 * (temp_desejada - temp_ambiente)

def calcula_filtragem(volume):
    return volume * 2.5

def in_comprimento():
    return float(input("Insira o comprimento (em cm): "))

def in_altura():
    return float(input("Insira a altura (em cm): "))

def in_largura():
    return float(input("Insira a largura (em cm): "))

def in_temp_ambiente():
    return float(input("Insira a temperatura ambiente (em °C): "))

def in_temp_desejada():
    return float(input("Insira a temperatura desejada (em °C): "))

# Recebendo as entradas do usuário
comprimento = in_comprimento()
altura = in_altura()
largura = in_largura()
temp_ambiente = in_temp_ambiente()
temp_desejada = in_temp_desejada()

# Calculando os resultados
volume = calcula_volume(comprimento, altura, largura)
potencia = calcula_potencia(volume, temp_desejada, temp_ambiente)
filtragem = calcula_filtragem(volume)

# Exibindo os resultados
print(f'Volume: {volume:.2f} litros')
print(f'Potência do termostato: {potencia:.2f} watts')
print(f'Filtragem necessária: {filtragem:.2f} litros por hora')