# Funções


# Declaração 
# def nome_func (param1, param2):
#   codigo a ser executado
def saudar ():
    print('Bom dia, Maria!')

# Função sem retorno, com parametro
# Parametro é a variavel presente na assinatura da fn
# Neste caso abaixo, o parametro é 'nome'
def imprimir_nome(nome):
    print(f'Nome: {nome}')



saudar()
# Argumento é a variavel passada da instancia da Fn, nesses casos, 'Lucas' e 'Joel'
imprimir_nome('Lucas')
imprimir_nome('Joel')

# Função com retorno, sem parametro
def gerar_saudcao():
    return 'Bom dia!'

print(gerar_saudcao())

# Função com retorno, com parâmetro
def gerar_saudacao_nome(nome):
    return f'Bom dia, {nome}!'
# Chamando função acima
print(gerar_saudacao_nome('Jorge'))


# O melhor caso a ser usado é com parametros e com retorno (ATENÇÃO), pois usa Fn's puras
# Função pura é uma função sem efeitos colaterais

#calcula a media de varios alunos
notas_alunos = [[10,6],[5,8],[9,5]]
def calcula_media(notas):
    return sum(notas)/len(notas)

def calcula_medias(notas_alunos):
    medias = []
    for notas in notas_alunos:
        medias.append(calcula_media(notas))
    return medias

def melhor_jeito_calcula_medias(notas_alunos):
    return[calcula_media(notas) for notas in notas_alunos]

print(melhor_jeito_calcula_medias(notas_alunos))



# Argumento nomeados
def nova_saudacao(nome, saudacao):
    return f'{saudacao}, {nome}!'

print(nova_saudacao(nome='Wellington Rato', saudacao='Bom dia'))

print('eu', 'ela', sep=' morte ')

# *args (Non-Keyboar Arguments)
def calcular_mediaaa(*notas):
    return sum(notas)/len(notas)


