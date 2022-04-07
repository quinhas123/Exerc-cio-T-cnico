import csv
from tabelaHash import TabelaHash
from Trie import *
from query import *
from entradas import *
from menu import *

clearConsole = lambda: print('\n' * 150)

if __name__ == "__main__":

    root = TrieNode('*')

    bolsas = TabelaHash()
    lista = bolsas.inicializa_dados(root)

    rodar = True
    rodar2 = True

    while rodar:
        rodar2 = True

        menu()

        try:

            ent = int(input("Digite um número correspondente a uma busca:"))

            if ent == 5:
                rodar = False
                break

            else:
                if ent == 1 or ent == 2 or ent == 3 or ent == 4:
                    numero(ent, bolsas, root, lista)

                    while rodar2:

                        try:
                            print()
                            print('1. [MENU]')
                            print('5. [Terminar o programa]')
                            entrada = int(input("Digite um número válido: "))

                            if entrada == 1:
                                clearConsole()
                                rodar2 = False

                            else:
                                if entrada == 5:
                                    rodar2 = False
                                    rodar = False

                            clearConsole()

                        except:
                            clearConsole()
                            pass

                else:
                    clearConsole()

        except ValueError:
            clearConsole()
            pass













