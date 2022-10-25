
data = []

attr1 = "Transaction ID"
attr2 = "List of items"

n = int(input("Enter the number of transactions : "))

items = []
for i in range(n):
	at1 = input("Enter the transaction ID : ")
	at2 = list(map(str, input("Enter the list of items associated with the given transaction ID : ").split(" ")))
	
	data.append([at1] + at2)
	for j in at2:
		if [j] not in items:
			items.append([j])
	

items.sort()
min_sup = int(input("Enter the minimum support value : "))

for i, j in enumerate(items):
	for k, l in enumerate(items):
		if k > i and len(j) == len(l):
			flag = 1
			for m in range(len(j) - 1):
				if j[m] != l[m]:
					flag = 0
					break
			if flag == 1:
				temp = []
				temp.extend(j)
				temp.append(l[len(l) - 1])
				if temp not in items:
					items.append(temp)

satissets = []
max_l = 0

for i in items:
	count = 0
	for df in data:
		flag1 = 1
		for k in i :
			flag2 = 1
			for l in df:
				if k == l:
					flag2 = 0
			if flag2 == 1:
				flag1 = 0
				break
				
		if flag1 == 1:
			count += 1
		
	if count >= min_sup:
		max_l = max(max_l, len(i))
		satissets.append([i, len(i), count])
		
ltables = [[] for i in range(max_l)]

for item in satissets : 
	ltables[item[1] - 1].append(item[0] + [item[2]])

print("")
for i, fsets in enumerate(ltables):
	x = "L" + str(i + 1)
	print("{:^50}".format(str(x)))
	print("--------------------------------------------------")
	print("|         Itemset          |     Support Count   |")
	print("--------------------------------------------------")
	for j in fsets:
		print("|{:^26}|{:^21}|".format(str(j[:len(j)- 1]), str(j[len(j) - 1])))	
	print("--------------------------------------------------")
	print("")
	
	




	
	

	
