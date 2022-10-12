
def printer(mat, number_of_vals):
    for i in range(number_of_vals):
        for j in range(i + 1):
            print("{0:.2f}".format(mat[i][j]), end = ' ')
        print(" ")

f = open('./Dataset1.txt', 'r')

data = {}
features = f.readline()
for i in features.strip().split():
    data[i] = []

keys = list(data.keys())

values = f.readlines()
number_of_vals = len(values)
for i in values:
    k = 0
    for j in i.split():
        data[keys[k]].append(j)
        k = k + 1


print("Enter the nominal attributes : ")
nom_attr = list(map(str, input().strip().split()))
print("Enter the numeric attributes : ")
num_attr = list(map(str, input().strip().split()))

#Find dissimilarity matrix of nominal and numeric attributes

disnom = [[0 for x in range(number_of_vals)] for x in range(number_of_vals)]
disnum = [[0 for x in range(number_of_vals)] for x in range(number_of_vals)]


for i in range(number_of_vals):
    for j in range(i + 1):
        m = 0
        e_dist = 0
        for k in nom_attr:
            if data[k][i] == data[k][j]:
                m = m + 1
        for k in num_attr:
            e_dist = e_dist + ((float(data[k][i]) - float(data[k][j])) ** 2)
        disnom[i][j] = (len(nom_attr) - m) / len(nom_attr)
        disnum[i][j] = e_dist ** 0.5

printer(disnom, number_of_vals)
printer(disnum, number_of_vals)

    
        

