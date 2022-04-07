from Trie import *
from tabelaHash import *

'''
queryTrie
Função recebe um 'root' e um 'prefixo' no formato:
    root: TrieNode()
    prefixo: string
A função verifica se o prefixo informado como caractere está no TrieNode. Se estiver, então é 
procurado todos os nomes presentes na TrieNode a partir do último nodo do prefixo. O retorno 
é um conjunto com o nome de todos com o prefixo informado em seu nome.    
'''

def queryTrie(root, prefixo:str):
    found = []

    tupla = acharPrefixo(root, prefixo.upper())

    if tupla[0] == True:
        acharNome(tupla[1], found)

    #ignora repetidos
    found = set(found)

    return found



'''
queryCbz
Função recebe uma 'lista' e um 'ano' no formato:
    lista: list
    ano: int
A função verifica se, para cada pessoa na lista, o ano de seu início de bolsa é igual 
ao ano passado como parâmetro, se for:
        -Retorna uma lista com certas informações da pessoa
Se não for:
        -Vai para a próxima pessoa da lista
'''

def queryCbz(lista, ano):

    for pessoa in lista:
        try:
            if pessoa[4] == ano:
                bolsista = [pessoa[0], pessoa[1], pessoa[2], pessoa[10]]

                return bolsista
        except:
            pass



'''
queryMedia
Função recebe uma 'tabela' e um 'ano' no formato:
    tabela: TabelaHash()
    ano: int
A função verifica se, para cada pessoa na tabela, o ano de seu início de bolsa é igual 
ao ano passado como parâmetro, se for:
        -Adiciona o seu valor de bolsa em a variável 'media'
        -Aumenta em um a variável 'cont'
Se não for:
        -Vai para a próxima pessoa da tabela
Quando é passado pro toda tabela, então é calculado a média dos valores das bolsas 
dividindo a variável 'media' por 'cont'. Esse valor é retornado.
'''

def queryMedia(tabela, ano):
    media = 0
    cont = 0

    for pessoa in tabela.table:

        try:
            if pessoa[4] == ano:
                media += pessoa[10]
                cont += 1

        except:
            pass

    result = media/cont
    return result



'''
queryRank
Função recebe uma 'tabela' no formato:
    tabela: TabelaHash()
Para cada pessoa na tabela, é adicionado seu 'nome' e 'valor de bolsa' no formato de lista
em uma lista. Após isso, é procurado qual pessoa tem o maior e menor 'valor de bolsa'. Ao final, 
essas pessoas são adicionadas a duas listas sepadaradas e excluídas da lista com todas as outras 
pessoas da tabela e o processo é repetido mais duas vezes. Por fim, é retornado uma lista com
os três alunos com os valores da bolsa mais altos e uma lista com os três alunos com os valores 
da bolsa mais baixos.
'''

def queryRank(tabela):
    hash_org = []

    for pessoa in tabela.table:

        try:
            list = []
            list.append(pessoa[0])
            list.append(pessoa[10])
            hash_org.append(list)

        except:
            pass

    found_maiores = []
    found_menores = []
    count = 0
    while count != 3:
        valor_max = [0, None]
        for elemento in hash_org:
            if valor_max[1] is None or elemento[1] > valor_max[1]:
                valor_max = elemento

        found_maiores.append(valor_max)
        hash_org.remove(valor_max)

        valor_min = [0, None]
        for elemento in hash_org:
            if valor_min[1] is None or elemento[1] < valor_min[1]:
                valor_min = elemento

        found_menores.append(valor_min)
        hash_org.remove(valor_min)

        count += 1

    return found_maiores, found_menores






