# String
nome = "Lucas Moura"
time = 'SPFC'
# Multilinha
musica = """MEU TRICOLOR
É CAMPEÃO
CHORA PORCADA, PEIXE, GAVIÃO"""

# Int
camisa = 7

# Booleano
lesionado = False
cdb = True

# float
idade = 31.7

# Interpolação 
print (f"Olá {nome}, Voce tem {idade} anos!")

# Pegando partes de string 
print(nome[5::])

# Lista 
titulos_mundiais = ['1992', '1993', '2005']
# Acesso_item
print(titulos_mundiais[2])
titulos_mundiais.insert(3,'2024')
print(titulos_mundiais)

for titulo in titulos_mundiais:
    print(titulo)


#Tuplas 
opcoes = ('sim', 'nao', 'talvez')

# set [conjunto]
# Não permite elementos duplicados
# Não é indexado

Naipes = {'Copas', 'Paus', 'Ouro', 'Espada'}
Naipes.add('Curinga')
print(Naipes)

# Dict (dicionario)
#palavra definicão
#key -> value
#

jogador = {
'nome' : nome,
'idade': idade,
'cdb': cdb,
'camisa': camisa
}
print(jogador)

# None
nome = None