from ps5 import *
def decrypt_story():
	#passando a mensagem a ser descriptografada (a mensagem é uma string que foi retirado do arquivo story.txt através de uma função)
	cipher = CiphertextMessage(get_story_string())
	return cipher.decrypt_message()

print(decrypt_story())	

