import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    #ignorar pontuação
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #alfabeto maiusculo e minusculo que serão as chaves do dicionario
        string_lower = string.ascii_lowercase
        string_upper = string.ascii_uppercase
        
        dic_values = {}
        #iterando sobre o alfabeto minusculo
        for letter in string_lower:
        	#verificando o valor de new_shift subtraindo o valor da letra na tabela ascii pelo valor da letra z
        	new_shift = (ord(letter) + shift) - ord("z")
        	#caso new_shift seja maior que zero significa que após aplicar o shift a letra excedeu o alfabeto e terá que começar de novo (voltar para a letra 'a')
        	if new_shift > 0:
        		dic_values[letter] = chr(ord("a") + (new_shift - 1))
        	else:
        		dic_values[letter] = chr(ord(letter) + shift)
        
        #aplicando a ideia anterior nas letras maiusculas
        for letter in string_upper:
        	#pegando a versão da letra maiuscula nas minusculas
        	dic_values[letter] = dic_values[letter.lower()].upper()
        return dic_values			

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #verificando se shift é um valor possivel para o alfabeto
        assert 0 <= shift < 26
        #a string criptografada
        new_string = ""
        for letter in self.message_text:
        	#se uma determinada letra da palavra fizer parte do alfabeto (que sera a unica coisa que iremos criptografar)
        	if letter in string.ascii_uppercase or letter in string.ascii_lowercase:
        		#aplicar a funçao build_shift_dict() para pegar a verão encriptada no dicionario
        		new_string += self.build_shift_dict(shift)[letter]
        	else:
        		#caso a letter seja um numero, espaço ou caractere especial apenas adiciona-lo a nova string
        		new_string += letter
        return new_string	

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        super().__init__(text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        #criando messagem criptografada
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        #build_shift_dict retorna um dicionario com as chaves sendo o alfabeto e o valor sendo a "nova letra" pós mover "shift" vezes
        #estou retornando uma copia
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):
	def __init__(self, text):
		'''
	    Initializes a CiphertextMessage object
	                
	    text (string): the message's text

	    a CiphertextMessage object has two attributes:
	    		self.message_text (string, determined by input text)
	            self.valid_words (list, determined using helper function load_words)
    	'''
    	#text = mensagem encriptada
		super().__init__(text)

	def decrypt_message(self):
		'''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
		#quantidade de palavras corretas em uma tentativa de descriptografar
		size = 0
		#chave final
		shift = 0
		#chave temporaria
		temp_shift = 1
		#mensagem que sera retornada
		mensagem = ""
		#testar todas as chaves
		while temp_shift <= 26:
			#variavel que vai contabilizar quantas palavras validas uma chave conseguiu fazer e verificar com as palavras validas anteriores
			temp = 0
			#tentando as chaves
			mensagem_temp = self.apply_shift(26 - temp_shift).split()
			for word in mensagem_temp:
				if is_word(self.valid_words, word):
					temp += 1

			#comparando qual tem mais palavras válidas
			if temp > size:
				size = temp
				mensagem = " ".join(mensagem_temp)
				shift = temp_shift
			temp_shift += 1

		return (26 - shift, mensagem)				


#Example test case (PlaintextMessage)
#plaintext = PlaintextMessage('Message is Nonsense words: confident step talk essence airplane one quarrel hole firm fact attention insurance indeed early lengthen', 13)
#print('Expected Output: jgnnq')
#print('Actual Output:', plaintext.get_message_text_encrypted())
#print(plaintext.get_message_text_encrypted())    
#Example test case (CiphertextMessage)
#ciphertext = CiphertextMessage(plaintext.get_message_text_encrypted())
#print(ciphertext.decrypt_message())
#print('Expected Output:', (24, 'okay am trying with more words'))
#print('Actual Output:', ciphertext.decrypt_message())
#print(is_word(load_words(WORDLIST_FILENAME), "a"))
#m = Message("jgnnq")
#print(m.apply_shift(26-2))
#print(m.build_shift_dict(4))
#print(m.apply_shift(3))
#plaintext.change_shift(4)
#print(plaintext.get_message_text_encrypted())
#print(plaintext.get_encrypting_dict())
#print(get_story_string())
