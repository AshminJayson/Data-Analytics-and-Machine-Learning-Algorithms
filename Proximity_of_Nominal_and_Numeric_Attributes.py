
f = open('./Dataset1.txt', 'r')

data = {}
features = f.readline()
for i in features.strip().split():
    data[i] = []

keys = list(data.keys())

values = f.readlines()
number_of_val = 0
for i in values:
    k = 0
    number_of_val = number_of_val + 1
    for j in i.split():
        data[keys[k]].append(j)
        k = k + 1


print("Enter the nominal attributes : ")
nom_attributes = list(map(str, input().strip().split()))
print("Enter the numeric attributes : ")
num_attributes = list(map(str, input().strip().split()))

#Find dissimilarity matrix of nominal attributes

disnom = [[0 for x in range(number_of_val)] for x in range(number_of_val)]
disnum = [[0 for x in range(number_of_val)] for x in range(number_of_val)]

for i in range(number_of_val):
    for j in range(i):
        m = 0
        e_dist = 0
        for k in nom_attributes:
            if data[k][i] == data[k][j]:
                m = m + 1
        for k in num_attributes:
            e_dist = e_dist + ((float(data[k][i]) - float(data[k][j])) ** 2)
        disnom[i][j] = (len(nom_attributes) - m) / len(nom_attributes)
        disnum[i][j] = e_dist ** 0.5

print(disnum)
print(disnom)


    
        

