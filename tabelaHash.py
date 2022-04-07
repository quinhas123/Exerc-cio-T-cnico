import csv
from Trie import *


'''
TabelaHash
Objeto criado com dois parâmetros: Um representa o tamanho da TabelaHash, que foi definido a do menor número primo mais 
próximo de de 120% das linhas utilizadas no arquivo .csv. Outro inicializa a TabelaHash.
'''

'''
hash_function
Função recebe como parâmetro uma 'palavra' no formato:
    palavra: string
A função calcula uma posição na TabelaHash baseado nos caracteres da 'palavra'
'''

'''
insert_hash
Função recebe como parâmetro um 'nome', 'cpf', 'uni', 'mes', 'ano', 'diret', 'sistorg', 'sgbmodal', 'pagmodal', 'moeda' 
e 'valor', no formato:
    nome: string
    cpf: string
    uni: string
    mes: int
    ano: int
    diret: string
    sistorg: string
    sgbmodal: int
    pagmodal: string
    moeda: string
    valor: int
A função, a partir do nome, chama a função 'hash_function' e calcula uma posição na TabelaHash. Sendo assim, verifica 
se essa posição está vazia. Se estiver, então:
        -Colocar uma lista com todos os parâmetros nessa posição calculada na TabelaHash.
Se não estiver, então:
        -Procurar se a próxima posição da TabelaHash está disponível. Se estiver:
                -Colocar uma lista com todos os parâmetros nessa posição calculada na TabelaHash.
            Se não estiver:
                -Procurar a próxima posição até achar.
'''

'''
query
Função recebe como parâmetro um 'nome' no formato:
    nome: string
A função procura na TabelaHash a posição dada pelo nome aplicado à função 'hash_function'. Caso o nome for igual ao 
'nome' da posição da pessoa da lista, então:
        -Retornar lista da posição.
Se não, então:
        -Procura a próxima posição na TabelaHash até achar.
        -Retornar lista da posição.
'''

'''
inicializa_dados
Função recebe como parâmetro 'root' no formato:
    root: TrieNode()
A função lê o arquivo 'br-capes-bolsistas-uab.csv' e, linha por linha, chama a função 'insert_hash' para guardar as
informações lidas. Além disso, chama a função 'inserirNaTrie' para inserir o parâmetro 'nome' da linha no root. Por
fim, retorna uma lista com todos os primeiros bolsistas de cada ano.
'''


class TabelaHash(object):

    def __init__(self):

        self.size = 96017
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, palavra:str):
        g = 31
        hash = 0
        for char in palavra:
            hash = g * hash + ord(char)
        return (hash & 0x7fffffff) % self.size

    def insert_hash(self, nome:str, cpf:str, uni:str, mes:int, ano:int, diret:str, sistorg:str, sgbmodal:int, pagmodal:str, moeda:str, valor:int):
        ocupado = True
        ocupado2 = True
        col = 1
        col2 = 0

        if self.table[self.hash_function(nome)] == []:
            self.table[self.hash_function(nome)] = [nome, cpf, uni, mes, ano, diret, sistorg, sgbmodal, pagmodal, moeda, valor]

        else:
            while ocupado == True:
                if self.table[self.hash_function(nome) + col] == []:
                    self.table[self.hash_function(nome) + col] = [nome, cpf, uni, mes, ano, diret, sistorg, sgbmodal, pagmodal, moeda, valor]
                    ocupado = False
                else:
                    if self.hash_function(nome) + col == 96016:
                        while ocupado2 == True:
                            if self.table[col2] == []:
                                self.table[col2] = [nome, cpf, uni, mes, ano, diret, sistorg, sgbmodal, pagmodal, moeda, valor]
                                ocupado2 = False

                            else:
                                col2 += 1
                        return
                    else:
                        col += 1

            return

    def query(self, nome:str):
        col=1
        col2=0
        not_found = True
        not_found2 = True

        if self.table[self.hash_function(nome)][0] == nome:
            return self.table[self.hash_function(nome)]
        else:
            while not_found == True:
                if self.table[self.hash_function(nome)+col][0] == nome:
                    return self.table[self.hash_function(nome)+col]
                else:
                    if self.hash_function(nome)+col == 96016:
                        while not_found2 == True:
                            if self.table[col2][0] == nome:
                                return self.table[col2]

                            else:
                                col2 += 1
                    else:
                        col += 1


    def inicializa_dados(self, root):

        with open('br-capes-bolsistas-uab.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')

            csv_reader.__next__()

            lista_primeiros = []
            ano2 = 2016
            for row in csv_reader:
                nome = str(row[0])
                cpf = str(row[1])
                uni = str(row[2])
                mes = int(row[3])
                ano = int(row[4])
                diret = str(row[5])
                sistorg = str(row[6])
                sgbmodal = int(row[7])
                pagmodal = str(row[8])
                moeda = str(row[9])
                valor = int(row[10])

                if ano != ano2:
                    lista_primeiros.append(bolsista)
                    ano2 -= 1

                bolsista = [nome, cpf, uni, mes, ano, diret, sistorg, sgbmodal, pagmodal, moeda, valor]


                self.insert_hash(nome, cpf, uni, mes, ano, diret, sistorg, sgbmodal, pagmodal, moeda, valor)
                inserirNaTrie(root, nome)

            lista_primeiros.append(bolsista)

        csv_file.close()

        return lista_primeiros
