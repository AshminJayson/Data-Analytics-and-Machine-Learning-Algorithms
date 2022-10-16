data = {}

attr1 = "Transaction ID"
attr2 = "List of items"

n = int(input("Enter the number of data points : "))

items = set()
for i in range(n):
	at1 = input("Enter the transaction ID : ")
	at2 = list(map(str, input("Enter the list of items associated with the input transaction ID : ").split(" ")))
	data[at1] = sorted(at2)
	for i in at2 : items.add([i])
	


min_sup = int(input("Enter the minimum support threshold value : "))


for i, j in enumerate(items):
	print(items)
	for k, l in enumerate(items):
		if l > j and len(i) == len(k) :
			flag = 1 
			for m in range(len(i) - 1):
				if i[m] != k[m]:
					flag = 0
					break
			if flag == 0 : 
				items.add([set(i + k)])
	 
			
	
	
