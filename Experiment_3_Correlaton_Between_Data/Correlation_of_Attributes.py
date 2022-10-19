#Not completed

print("Enter the number of numeric values") 

n = int(input("Enter the number of data points : "))

data = []

suma, sumb, meana, meanb, prodab, vara, varb = 0, 0, 0, 0, 0, 0, 0

for i in range(n):
	temp = list(map(int, input("Enter the data point : ").split()))
	data.append(temp)
	suma += temp[0]
	sumb += temp[1]
	
meana = suma / n
meanb = sumb / n

for i in range(n):
	vara += (data[i][0] - meana) ** 2
	varb += (data[i][1] - meanb) ** 2
	prodab += data[i][0] * data[i][1]
	
vara /= n
varb /= n
sda = vara ** 0.5
sdb = varb ** 0.5

corrcoff = prodab / (n * sda * sdb)

print("The correlation coefficient is : ", corrcoff)
	
