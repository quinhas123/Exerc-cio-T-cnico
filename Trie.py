'''
TrieNode
Objeto criado com seis parâmetros:
    char: string - representa o caractére do nodo.
    filhos: list - lista com os filhos do nodo.
    fimdepalavra: boolean - informa se aquele nodo representa se é o fim de uma palavra.
    nome: string - string com a palavra inteira até aquele nodo.
    contador: int - número com quantidade de nodos embaixo dele mais ele mesmo.
    folha: boolean - informa caso o caráctere for uma folha na árvore.
Objeto criado com o intuito de criar uma árvore Trie, para possibilitar a pesquisa de nomes por prefixo.
'''


class TrieNode():

    def __init__(self, char: str):
        self.char = char
        self.filhos = []
        self.fimdepalavra = False
        self.nome = ''
        self.contador = 1
        self.folha = False



'''
inserirNaTrie
Função recebe como parâmetro um 'word' e um 'root' no formato:
    word: string
    root: TrieNode()
A função insere cada caractére no nodo root. Sendo assim, para cada caractére em word, verifica se os filhos do
nodo root já possuem o caractér. Se os filhos de root já possuem o caractér, então adiciona um ao contador e passa para
o próximo caractér e nodo. Se os filhos de root não possuem o caractér, então adiciona um nodo no filho de root e 
adiciona a palavra inteira a partir desse caractér. Quando chegar ao fim, atualiza os campos 'fimdepalavra' e 'nome' 
do último nodo para seus respectivos valores.
'''


def inserirNaTrie(root, word:str):
    node = root
    for char in word:
        found_in_child = False

        for filho in node.filhos:
            if filho.char == char:
                filho.contador += 1
                node = filho

                if node.folha == True:
                    node.folha = False

                found_in_child = True
                break

        if not found_in_child:
            novo_nodo = TrieNode(char)
            node.filhos.append(novo_nodo)

            node = novo_nodo

    if len(node.filhos) == 0:
        node.folha = True

    node.fimdepalavra = True
    node.nome = word



'''
acharPrefixo
Função recebe como parâmetro um 'prefixo' e um 'root' no formato:
    prefixo: string
    root: TrieNode()
A função procura no nodo root, caractére por caráctere, se existe o caractére nos filhos de root. Se existir, então
passa para o nodo do caráctere achado e é procurado em seus filhos se existe o próximo caractére. Isso continua até 
achar todos os caractéres do prefixo. Se achar, então:
        -Retorna um boolean 'True' e o nodo do último caractére do prefixo. 
Se não achar, então:
        -Retorna um boolean 'False' e um int '0'
'''


def acharPrefixo(root, prefixo:str):
    node = root

    if not root.filhos:
        return False, 0

    for char in prefixo:
        char_not_found = True

        for filho in node.filhos:
            if filho.char == char:
                char_not_found = False

                node = filho
                break

        if char_not_found:
            return False, 0

    return True, node



'''
acharNome
Função recebe como parâmetro um 'found' e um 'node' no formato:
    found: list
    node: TrieNode()
A função procura todas as palavras que existem a partir do nodo informado. Sendo assim, primeiro é verificado se
o nodo 'node' em si representa uma palavra. Caso representar, adicionar a palavra em found e verificar se é folha. 
Após isso, verificar se cada filho de node são folhas. Se for, então adicionar a palavra em found e ir para o próximo 
filho. Nesse mesmo laço, verificar se o seu contador é diferente de 0. Se for, chamar a recursão e verificar se seu 
valor é diferente de vazio. Se for, adicionar a a palavra em found.
'''
def acharNome(node, found):

    if node.fimdepalavra == True:
        found.append(node.nome)

        if node.folha == True:
            return

    for filho in node.filhos:
        if filho.folha == True:
            found.append(filho.nome)
            break

        if filho.contador != 0:
            aux = acharNome(filho, found)
            if aux != '':
                found.append(aux)

    return filho.nome

