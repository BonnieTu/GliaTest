import sys
from math import sqrt

num = int(input("Please input a number:"))
max_prime_factor = 0
i = 2
while i<num:
	isfactor = 0
	if num%i==0:
		isfactor = 1
		num /= i
	if isfactor:
		isprime = 1
		isprimenum = 1
		for x in range(2,int(sqrt(i))):
			if i%x==0:
				isprime=0
				break
		for x in range(2,int(sqrt(num))):
			if num%x==0:
				isprimenum = 0
				break
		if isprime:
			if(isprimenum):
				if(num>i):
					max_prime_factor=int(num)
				else:
					max_prime_factor = i
		if num == 1:
			break
	i += 1

print(max_prime_factor)