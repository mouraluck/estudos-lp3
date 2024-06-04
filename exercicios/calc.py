def calcula_volume (comprimento,altura,largura) :
    return (comprimento * altura * largura) / 1000

def calcula_potencia (volume, temp_desejada, temp_ambiente):
    return volume * 0.05 * (temp_desejada - temp_ambiente)

def calcula_filtragem (volume):
    return volume*2,3