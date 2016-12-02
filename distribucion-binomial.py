def nbin(n,k,p):
	from scipy.special import binom
	return binom(n-1,k-1)*p**k*(1-p)**(n-k)
