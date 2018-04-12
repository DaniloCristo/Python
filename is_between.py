#função que checa se o valor de n2 esta entre o n1 e o n3
def is_between(n1,n2,n3):
	if n1<= n2 <= n3:
		return "Yes, {0} is between {1} and {2}".format(n2,n1,n3)
	else:
		return "No it is not"	

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))

print(is_between(n1,n2,n3))		