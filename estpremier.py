def est_premier(n):
	if (n<=1): return False
	k = 2
	while k*k <= n:
		if n%k==0:
			return False
		else:
			k = k +1
			return True

print("TEST: est_premier(20)")
print("Le nombre 20 est il premier ?:"+str(est_premier(20)))

print(print("TEST: est_premier(7)"))
print("Le nombre 7 est il premier ?:"+str(est_premier(7)))