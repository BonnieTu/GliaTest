import sys

first = 990
second = 33
result = 1

for x in range(1,second+1):
	result *= (first-x+1)
	result /= x

print(int(result))