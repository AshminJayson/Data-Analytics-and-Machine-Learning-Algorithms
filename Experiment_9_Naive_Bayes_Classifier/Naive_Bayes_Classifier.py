from tabulate import tabulate
from collections import Counter
import statistics as st
import math

def probNomEval(subset, val, ind):
    count = Counter([k[ind] for k in subset])
    return count[val]/len(subset)

def probNumEval(subset, val, ind):
    
    stat = [k[ind] for k in subset]
    mean = st.mean(stat)
    std = st.stdev(stat)
    z = (1 / ((2 * math.pi) ** 0.5 * std)) * math.e ** (-1 * ((val - mean) ** 2) / (2 * std))
    return z

    

def classify(dataset, x, tableheader, types, y):
    classIndex = len(types) - 1
    prob = 1
    for i in range(len(x)):
        
        if types[i] == 'NOM':
            subset = [k for k in dataset if k[classIndex] == y]
            # print(subset)
            pr = probNomEval(subset, x[i], i)
            print('Probability of ', tableheader[i], ' : ', x[i], ' given ', y , ' is : ', pr)
            prob *= pr

        else:
            subset = [k for k in dataset if k[classIndex] == y]
            for ind, item in enumerate(subset):
                subset[ind][i] = int(subset[ind][i])
            pr = probNumEval(subset, x[i], i)
            print('Probability of ', tableheader[i], ' : ', x[i], ' given ', y , ' is : ', pr)
            prob *= pr

    return prob

f = open('./testdata.txt', 'r')

types = f.readline().strip().split(',')
tableheader = f.readline().strip().split(',')

lines = f.readlines()

dataset = []

for line in lines:
    dataset.append(line.strip().split(','))

print(types)
# print(tableheader)
# print(tabulate(dataset))

x = [42,'HIGH','NO','FAIR']

pyes = classify(dataset, x, tableheader, types, 'YES')
print('\n--------------------------------\n')
pno = classify(dataset, x, tableheader, types, 'NO')

yesno = Counter([k[len(types) - 1] for k in dataset])
pyes *= yesno['YES']/len(dataset)
pno *= yesno['NO']/len(dataset)

if pyes > pno:
    print('Probability of YES  :  given ', x , ' : ', pyes , ' is greater than Probability of NO given ', x , ' : ',  pno)
else:
    print('Probability of NO :  given ', x , ' : ', pno , ' is greater than Probability of YES given ', x , ' : ',  pyes)
