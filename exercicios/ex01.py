'''
Ex01. Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

    O volume do aquário em litros;
    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

    Volume é dado por (comprimento * altura * largura) / 1000
    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.'''

from calc import calcula_filtragem,calcula_potencia,calcula_volume
from entradas import in_altura,in_comprimento,in_largura

largura = in_largura
altura = in_altura
comprimento = in_comprimento

volume = calcula_volume(comprimento, altura, largura)
print(volume)
print(calcula_potencia(volume,te))
