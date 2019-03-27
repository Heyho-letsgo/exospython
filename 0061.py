# coding: utf-8



n = int(input("Saisissez un integer : "))
print (n)
m = n
i = 0

if n % 2 == 0:
	print ("le nombre saisi est pair") 
	while n % 2 == 0:
		n = n/2
		
		i +=1
	print( m, " est divisible ", i, "fois par 2.")
	



else:
	print ("le nombre saisi est impair")

i = 0
print (m)
print (i)
n = m
try:
	while i != m:
		if m % m == 0: 
			m -= 1
			i += 1
	print ("i  = ",i)
	if i > 2:
		print (n, " n'est pas premier")
except ZeroDivisionError:
	print (n, " est  premier")
