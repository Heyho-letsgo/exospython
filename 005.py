"""
Enter a number n and count the number of
times that number is divisible by 2.
"""


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

	


