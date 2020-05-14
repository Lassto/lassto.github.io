def euclide_etendu(a,b):
	x = 1 ; xx = 0
	y = 0 ; yy = 1
	while b != 0 :
		q = a // b
		a , b = b , a % b
		xx , x = x - q*xx , xx
		yy , y = y - q*yy , yy
	return (a,x,y)

def inverse(a,n):
	c,u,v = euclide_etendu(a,n) # pgcd et coeff. de Bézout
	if c != 1 : # Si pgcd différent de 1 renvoie 0
		return 0
	else :
		return u % n # Renvoie l'inverse

#TEST, on veut calculer l'inverse de 7 modulo 15 , cad touver x tel 7*x = 1 mod 15 
print("inverse de 7 mod 15 est :"+ str((inverse(7,15))))