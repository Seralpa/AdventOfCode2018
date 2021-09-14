import math

# num extracted from analizing input
num = 10551358
lim = math.sqrt(num)
sum = 0
for i in range(1, int(lim)):
	if num % i == 0:
		sum += i
		sum += num / i
print(int(sum))