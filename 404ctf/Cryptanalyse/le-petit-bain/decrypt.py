OUTPUT = "C_ef8K8rT83JC8I0fOPiN6P!liE03W2NXFh1viJCROAqXb6o"

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"

def f(a,b,n,x):
	return (a*x+b)%n

def f_inv(a,b,n,x):
	return ( (x-b%n) * pow(a,-1,n))