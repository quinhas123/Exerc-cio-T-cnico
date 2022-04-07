import csv
from tabelaHash import *
from Trie import *
from query import *
from entradas import *


'''
codifica
Função recebe um 'word' no formato:
    word: string
A função separa a 'word' em strings diferentes em uma lista (separação por ' '). Depois disso, para cada palavra dessa lista
é criada outra lista com cada caractere dessa palavra. Então, é substituído o primeiro caractere pelo último. Logo após, se
o tamanho da lista com os caracteres for maior que três, então reverter a lista. Por fim, é aumentado o valor ASCII de cada 
caractere da lista em um e é retornado uma string com todas as listas concatenadas.
'''


def codifica(word:str):
    lista = word.split()
    traducao = ''

    for elemento in lista:
        lista2 = list(elemento)

        aux = lista2[0]
        lista2[0] = lista2[len(lista2)-1]
        lista2[len(lista2) - 1] = aux

        if len(lista2) > 3:
            lista2.reverse()

        for elem in lista2:
            elem = chr(ord(elem)+1)

            if elem == '[':
                elem = 'A'

            traducao = traducao + elem

        traducao = traducao + ' '

    return traducao




