# partir de N calcule son écriture décimale [a0, a1, . . . , an].

def chiffres_vers_entier(tab):
	N = 0
	for i in range(len(tab)):
		N = N + tab[i] * (10 ** i)
	return N