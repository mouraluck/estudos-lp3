# if , if else, if elif

idade = 2

if idade>= 18:
    print("maior de idade")


#if/else
    if idade>= 18:
        print("Pode dirigir")
    else:
        print("Não pode dirigir")

#If/else/elif
        emancipado = True
        if idade>=18:
            print("Pode dirigir")
        elif emancipado:
            print("Pode dirigir")
        else:
            print("Não pode dirigir")

# if alinhado
user = "lulu"
senha = "123"

if user == "lulu" and senha == "123":
    print("Acesso permitido")
else:
    print("Acesso negado")
moradia = 2
moradias = {
    1: "casa",
    2: "apartamento",
    3: "rua"
}
if moradia in moradias:
    print(moradias[moradia])