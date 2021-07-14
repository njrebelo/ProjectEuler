#Considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#The A«answer should be 4613732

fib1 = 1
fib2 = 1
summ=0
result=0
while result < 4000000:
	result = (fib1+fib2)
	fib2=fib1
	fib1=result
	if (result%2) == 0:
		summ+=result
print(summ)
