# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
WORDLIST_FILENAME = "words.txt"

#retorna uma lista com as palavras no arquivo txt
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

#retorna uma das palavras (string) passadas como lista
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#retorna true caso todas as letras de secretWorld estejam em lettersGuessed
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return all(i in lettersGuessed for i in secretWord)

#retorna uma string com as letras que não estão em lettersGuessed substituidas por um "_" (underscore)
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    tempWord = secretWord
    for i in tempWord:
    	if i not in lettersGuessed:
    		tempWord = tempWord.replace(i,"_ ")
    return tempWord	

#retorna uma nova string com as letras que não estiverem em lettersGuessed   	
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alpha = string.ascii_lowercase
    s_retorno = ""
    for i in alpha:
    	if i not in lettersGuessed:
    		s_retorno += i
    return s_retorno
   

def hangman(secretWord):
	
	'''
    	secretWord: string, the secret word to guess.

    	Starts up an interactive game of Hangman.

    	* At the start of the game, let the user know how many 
    	  letters the secretWord contains.

  		* Ask the user to supply one guess (i.e. letter) per round.

   		* The user should receive feedback immediately after each guess 
     	about whether their guess appears in the computers word.

    	* After each round, you should also display to the user the 
      	partially guessed word so far, as well as letters that the 
      	user has not yet guessed.

    	Follows the other limitations detailed in the problem write-up.
	'''
    # FILL IN YOUR CODE HERE...
	numberGuess = 8
	print("Welcome to the game, hangman")
	print("I am thinking of a word that is {} letters long".format(len(secretWord)))
	print("-----------")
	#começando o loop
	while numberGuess > 0:
		print("You have {0} guesses left".format(numberGuess))
		print("Available Letters: {0}".format(getAvailableLetters(lettersGuessed)))
		letter = input("Please guess a letter: ")
		if letter in lettersGuessed:
			#caso ja tenha dado este palpite
			print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord,lettersGuessed)))
		elif letter not in secretWord:
			lettersGuessed.append(letter)
			print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord,lettersGuessed)))
			numberGuess -= 1
		else:
			lettersGuessed.append(letter)
			print("Good guess: {0}".format(getGuessedWord(secretWord,lettersGuessed)))
		#teste
		print("-----------")
		if isWordGuessed(secretWord, lettersGuessed):
			print("Congratulation, you won!")
			break
	#caso acabe as tentativas		
	if numberGuess == 0:
		print("Sorry, you ran out of guesses. The word was: {0}".format(secretWord))		
			
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#numberGuess = 8
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
#secretWord = "apple"
#hangman(secretWord)
lettersGuessed = []
#numberGuess = 8
availableLetters = getAvailableLetters(lettersGuessed) 
print(secretWord)
hangman(secretWord)
#print(isWordGuessed(secretWord,lettersGuessed))