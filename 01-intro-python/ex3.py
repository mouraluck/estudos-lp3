valor = float (input ("digite o valor comprado"))


if valor >= 10.00 and valor <= 99.99:
    valorfinal = valor - (valor * 0.05)
    print ("Valor final: " + valorfinal)
elif valor >= 100.00 and valor <= 499.99:
    valorfinal = valor - (valor * 0.1)
    print ("Valor final: " + valorfinal)
elif valor >= 500.00:
    valorfinal = valor - (valor * 0.15)
    print ("Valor final: " + valorfinal)
else:
    print ("Valor final: " + valor)