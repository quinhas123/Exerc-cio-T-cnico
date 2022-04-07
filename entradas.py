from Trie import *
from tabelaHash import *
from query import *
from codific import *

clearConsole = lambda: print('\n' * 150)

'''
numero
Função Função recebe um 'num', uma 'tabela', um 'root' e uma 'lista' no formato:
    num: int
    tabela: TabelaHash()
    root: TrieNode()
    lista: list
A função verifica se o 'num' passado como parâmetro é igual a 1, 2, 3, 4 ou 5. Se 'num' for igual 
a 1, então:
        -Receber input
        -Verificar se input é válido. Se não for:
                -Imprimir mensagem de entrada inválida.
            Se for, então:
                -Chamar a função 'queryCbz' e imprimir retorno.
Se 'num' for igual a 2, então:
        -Receber input
        -Chamar função 'queryTrie' com valor de input e verificar se o retorno é vazio. Caso for:
                -Imprimir mensagem de retorno vazio.
            Caso não for:
                -Cria uma lista de listas com as informações da tabela de cada pessoa do retorno.
                -Cria uma lista de lista com o nome codificado (através da função 'codifica'), ano, 
entidade de ensino, valor da bolsa.
                -Imprimir esta última lista criada.
Se 'num' for igual a 3, então:
        -Receber Input.
        -Verificar se input é válido. Se não for:
                -Imprimir mensagem de entrada inválida.
            Se for, então:
                -Chamar a função 'queryMedia' e imprimir retorno.
Se 'num' for igual a 4, então:
        -Chamar a função 'queryRank' e imprimir retorno.
Se 'num' for igual a 5, então:
        -Sair
'''


def numero(num:int, tabela:object, root, lista):

    if num == 1:


        try:
            clearConsole()
            entrada = int(input("Digite o ano que deseja consultar:"))

            if entrada < 2013 or entrada > 2016:
                print("Ano inválido!")
                return

            else:
                bolsista = queryCbz(lista, entrada)
                print(bolsista)

                return
        except:
            pass

    else:

        if num == 2:

            try:
                clearConsole()
                entrada = str(input("Digite um nome ou prefixo:"))

                found = queryTrie(root, entrada)

                if found == set():
                    print("Nenhum bolsista encontrado!")

                    return

                else:
                    found.discard('')

                    lista_nomes = []
                    lista_bolsistas = []
                    lista_final = []
                    for elem in found:
                        lista_nomes.append(elem)

                    for elemento in lista_nomes:
                        bolsista = tabela.query(elemento)

                        lista_bolsistas.append(bolsista)

                    for pes in lista_bolsistas:
                        lista_final_aux = [codifica(pes[0]), pes[4], pes[2], pes[10]]

                        lista_final.append(lista_final_aux)

                    for pessoa in lista_final:
                        print(pessoa)

                    return

            except:
                pass

        else:

            if num == 3:

                try:
                    clearConsole()
                    entrada = int(input("Digite o ano que deseja consultar:"))

                    if entrada < 2013 or entrada > 2016:
                        print("Ano inválido!")
                        return

                    else:
                        media = queryMedia(tabela, entrada)
                        print(media)

                        return

                except:
                    pass

            else:
                try:
                    clearConsole()
                    tupla = queryRank(tabela)
                    print("Três alunos com maiores valores de bolsa:")
                    print(tupla[0])
                    print()
                    print("Três alunos com menores valores de bolsa:")
                    print(tupla[1])

                    return

                except:
                    pass



