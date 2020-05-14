def pgcd(a,b):
	if a%b == 0:
		return b
	else:
		return pgcd(b, a%b)

print("Le pgcd(5,25) est "+str(pgcd(5,25)))