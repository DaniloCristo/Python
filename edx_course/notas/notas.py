
def get_data():
	'''
	Lê um arquivo csv e retorna uma lista onde o nome e as notas sao elementos
	'''
	file_name = "dados.csv"
	data = []
	try:
		file = open(file_name)
	except IOError:
		print("Não foi possivel abrir o arquivo.")
	else:
		#criando a lista
		next(file)
		for line in file:
			word = line.strip().split(",")
			data.append(word)
		return data
	finally:
		file.close()
dados = get_data()

def get_media(data):
	'''
	data: lista com o nome e as notas do estudante
	retorna: uma lista com o nome e a media do estudante
	'''
	media = []
	try:
		for student in data:
			media_estudante = (float(student[1]) + float(student[2])) / 2
			media.append([student[0], media_estudante])
	except IndexError:
		#caso um dos alunos esteja com os dados incompletos só adicionar o nome
		media.append([student[0]])
	return media			

media = get_media(dados)

def csv_media(media):
	'''
	media: lista com nome e a media do aluno
	criar um csv com esses dados
	'''
	file = open("media.csv","w")
	file.write("Nome, Media \n")
	for student in media:
		try:
			file.write("{}, {} \n".format(student[0], student[1]))
		except IndexError:
			file.write("{} \n".format(student[0]))

csv_media(media)						