def generateFile():
    '''
    abre o arquivo de texto e retorna uma lista com cada indice sendo uma   palvra
    '''
    file = open("palavras.txt", "r")
    string = file.read().split("\n")
    return string
#GLOBAL VARIABLE
l1 = generateFile()


def generateWord(l1):
    '''
    l1: lista com todas as palavras do arquivo
    retorna: uma das plavaras de forma aleatoria
    '''
    import random
    rand = random.randint(0, len(l1))
    return l1[rand]

def menu():
    '''
    Menu do game
    '''
    print("SELECIONE UMA OPÇÃO: ")
    print("=" * 10)
    print("1- jogar")
    print("2- Ver pontuacoes: ")
    print("3- Sair.")
    print("=" * 10)
    choice = int(input())
    return choice
def isCorrect(ans, word):
    '''
    retorna True caso a resposta dada esteja correta
    '''
    return ans == word

def game():
    '''
    exibir uma palavra para o usuario, pegar sua resposta e verificar se esta correta
    '''
    import time
    pontuacao = 0
    tot_words = 0
    end = time.time() + 10
    while end > time.time():
        word = generateWord(l1)
        tot_words += 1
        print(word)
        ans = input(":")
        if end > time.time() and isCorrect(ans, word):
            pontuacao += 1
    print(pontuacao)
def main():
    '''
    função responsavel por inicializar o jogo
    '''
    while True:
        choice = menu()
        if choice == 3:
            break
        elif choice == 1:
            game()
game()
