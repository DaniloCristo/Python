#Adivinhar numero pensado pelo o usuario através de tentativa e erro usando a busca binaria

print("Think in a number between 0 and 100!")
low = 0
high = 100

while True:
	guess = (high + low) // 2
	print("Is your secret number {0}?".format(guess))
	ans = input("Enter h to indicate the guess is too high. l to indicate the guess is too low. Or c to indicate the guess is correct")
	if ans == "l":
		low = guess
	elif ans == "h":
		high = guess
	elif ans == "c":
		break
	else:
		print("Sorry, i did not understand your input")	

print("Your secret number was: {0}".format(guess))				
