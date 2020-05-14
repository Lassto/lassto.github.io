#
# Pour tester  cette fonction: binaire_vers_entier([1,1,0])
#
def binaire_vers_entier(tab):
	N = 0
	for i in range(len(tab)):
		N = N + tab[i] * (2 ** i)
	return N

print("TESTING STEP\n")
#print("Le binaire de [1,1,0] est: "+binaire_vers_entier([1,1,0]))
print(binaire_vers_entier([1,1,0]))