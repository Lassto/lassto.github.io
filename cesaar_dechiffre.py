#Ici x est un nombre de f0, 1, . . . , 25g et k est le décalage. (x+k)%26 renvoie le reste modulo 26 de la somme(x+k). Pour le décryptage, c’est aussi simple :

def cesar_dechiffre_nb(x,k):
	return (x-k)%26