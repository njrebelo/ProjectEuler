#Our goal is to find the highest prime factor of a given number
#for this problem it will be 600851475143
#but for fun I have done an input so you can play around with it

targetNumber=vectorNumber=int(input("Wich number highest prime factor do you wan to calculate: ")) #we are goin to set our target number and the dividend for our operations
numbers=1 #Variable to iterate numbers
highestPrime=0 #Variable to store the highest prime


def test_prime(n):#Function to test a number as prime
    if (n==1): #1 is not prime
        return False
    elif (n==2): #2 is prime
        return True;
    else:
        for x in range(2,n): #for a number to be prime it cannot be divisable by anyother number but himslef and 1
            if(n % x==0):
                return False
        return True 

while (vectorNumber>1): #When the remainder of the division is 1 we have found our highest prime number
	if(test_prime(numbers)==True) and ((vectorNumber%numbers)==0) :
		highestPrime=numbers #save the prime number as the curent highest
		vectorNumber=(vectorNumber/numbers) #we do the division and update the dividend
	else:#if the number we are watching is not prime or is not mutiple of the target number we ignore it
		pass
	numbers+=1 #update the number
print(highestPrime,"is the highest prime factor")
