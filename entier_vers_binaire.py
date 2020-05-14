import math

def entier_vers_binaire(N):
	tab = []
	n = math.floor(math.log(N,2)) # le nombre de chiffres est n+1
	for i in range(0,n+1):
		tab.append((N // 2 ** i) % 2)
	return tab


# TEST

print("TEST de la fonction entier_vers_binaire(4)")
print(entier_vers_binaire(4))