#Operadores aritimetricos
# +, -, /, *, %, **


# Operadores logicos 
## and, or , not
print(True and False) # false

print(True or False) #true

lucasIsMan = True
lucasIsGay = True
lucasInMayor = False
lucasIsAnActor = True

#Nao pode ir a boate gay

if(lucasIsMan and lucasIsGay and lucasInMayor) or lucasIsAnActor:
    print("Lucas pode ir a boate gay")
else:
    print("Lucas não pode ir a boate gay")

    # Operadores de comparação 
    # ==, != , >, <, >=, <=


    def soma (n1,n2):
        return n1+n2
    
    # Operador IsNot, Is
    # Operadpr de identidade
    # Comparar se os objetos são os mesmos
    # mesmo espaço de memoria

    a = [1,2,3]
    b = [1,2,3]

    print(a==b)

    print(a is b) #False

    opcoes = ('sim', 'nao', 'talvez')
    opcao = input("Digite uma opção")
    opcao = opcao.lower().strip

    if opcao in opcoes:
        print("ok")
    else:
        print("invalido")