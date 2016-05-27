import sys

num = 1000
firstfactor = 3
secondfactor = 5
result = 0

for x in range(1,num):
	if x%firstfactor==0:
		result+= x
	if x%secondfactor==0 and x%firstfactor !=0:
		result += x
print(result)