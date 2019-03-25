n = int(input("Saisissez un integer : "))
print (n)
m = n
t =[]
i = 0
if n % 2 == 0:
	print ("le nombre saisi est pair") 
	while n % 2 == 0:
		n = n/2
		t.append(int(n))
		i +=1
	print( m, " est divisible ", i, "fois par 2.")
	print (t)
else:
	print ("le nombre saisi est impair")

