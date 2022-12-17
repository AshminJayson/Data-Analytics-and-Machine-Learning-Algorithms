import math
import copy 
from tabulate import tabulate 
from collections import Counter

class node:

    def __init__(self, dataset, attributelist, tableheader, splittingAtr, splitCondition):
        self.dataset = dataset
        self.attributelist = attributelist
        self.tableheader = tableheader
        self.children = []
        self.splittingAtr = splittingAtr
        self.splitCondition = splitCondition

def classifier(root, dataset, attributelist, tableheader):
    
    classDict = Counter([i[len(dataset[0]) - 1] for i in dataset])


    if len(classDict) == 1 or len(attributelist) == 1 or len(dataset) == 0:
        return

    samplecount = len(dataset)
    ebf = sum([classDict[i]/samplecount * math.log(classDict[i]/samplecount, 2) for i in classDict]) * -1

    mgain = 0
    splittingattribute = ""
    fixmean = 0


    for atr in attributelist:


        index = tableheader.index(atr)
        informationgainforattribute = 0

       
        if (isinstance(dataset[0][index], (int, float))):
            dataset.sort(key=lambda x : x[index])
            mean = 0
            ifgainSet = 100000000
            for i in range(len(dataset) - 1):
                mean = (dataset[i][index] + dataset[i + 1][index]) / 2
                upper = [i for i in dataset if i[index] <= mean]
                lower = [i for i in dataset if i[index] > mean]

                def rangeeval(sectionSet, sectionDict):
                    return sum([sectionDict[i]/len(sectionSet) * math.log(sectionDict[i]/len(sectionSet), 2) for i in sectionDict]) * -1

                upperDict = Counter([i[len(upper[0]) - 1] for i in upper])
                lowerDict = Counter([i[len(lower[0]) - 1] for i in lower])

                
                tempgainSet = (len(upper)/len(dataset) * rangeeval(upper, upperDict)) + (len(lower)/len(dataset) * rangeeval(lower, lowerDict))

                if tempgainSet < ifgainSet:
                    ifgainSet = tempgainSet
                    fixmean = mean 
                
                
            
            if ebf - ifgainSet > mgain:
                mgain = ebf - ifgainSet
                splittingattribute = atr

        else:
            atrvar = Counter([i[index] for i in dataset])
            for k in atrvar:

                datasetPart = [l for l in dataset if l[index] == k]
                tclassDict = Counter([i[len(datasetPart[0]) - 1] for i in datasetPart])

                infogaindj = 0
                tsamplecount = len(datasetPart)

                infogaindj = sum([tclassDict[i]/tsamplecount * math.log(tclassDict[i]/tsamplecount, 2) for i in tclassDict]) * -1
                informationgainforattribute += (atrvar[k] / samplecount) * infogaindj

        # print(informationgainforattribute, "attribute : ", i)

            if ebf - informationgainforattribute > mgain:
                mgain = ebf - informationgainforattribute
                splittingattribute = atr
    
    # print(splittingattribute)
    attributelist.remove(splittingattribute)
    index = tableheader.index(splittingattribute)
    tableheader.pop(index)
    atrvar = Counter(i[index] for i in dataset)
    
    if (isinstance(dataset[0][index], (int, float))):
        print('fxmena', fixmean)
        upper = [i[:index] + i[index + 1:] for i in dataset if i[index] <= fixmean]
        lower = [i[:index] + i[index + 1:] for i in dataset if i[index] > fixmean]

        print(upper,'\n\n',lower)
        tempnode1 = node(upper, attributelist, tableheader, splittingattribute, '<=' + str(fixmean))
        tempnode2 = node(lower, attributelist, tableheader, splittingattribute, '>' + str(fixmean))
        root.children.extend([tempnode1, tempnode2])
        classifier(tempnode1, copy.deepcopy(upper), copy.deepcopy(attributelist), copy.deepcopy(tableheader))
        classifier(tempnode2, copy.deepcopy(lower), copy.deepcopy(attributelist), copy.deepcopy(tableheader))
        pass
    else:
        for k in atrvar:
            datasetPart = [l[:index]+l[index+1:] for l in dataset if l[index] == k]    

            # print(datasetPart,"--------------")
            tempnode = node(datasetPart, attributelist, tableheader, splittingattribute, k)
            root.children.append(tempnode)
            classifier(tempnode, copy.deepcopy(datasetPart), copy.deepcopy(attributelist), copy.deepcopy(tableheader))

    

       
def printer(treestack):

    while(len(treestack) != 0):
        curr = treestack.pop(0)
        if curr == 100:
            print("next level")
            continue

        
        print("Splitting Attribute : ", curr.splittingAtr)
        print("Split Condition : ", curr.splitCondition)
        print(tabulate(curr.dataset,headers=curr.tableheader, tablefmt="outline"))
        for i in curr.children:
            treestack.append(i)
        treestack.append(100)
    

 

def main():

    f = open('testdata2.txt', 'r')
    # f = open('testdata.txt', 'r')


    attributelist = list(f.readline().strip().split(' '))
    tableheader = list(f.readline().strip().split(' '))
    # print(attributelist)

    lines = f.readlines()
    dataset = []
    for line in lines:
        dataset.append(line.strip().split(' '))

    for i in dataset:
        for ind, j in enumerate(i):
            try:
                i[ind] = int(i[ind])
            except:
                pass

    print(tabulate(dataset,headers=tableheader ,tablefmt='outline'))
    root = node(dataset, attributelist,tableheader, "No Split", "No Split")
    classifier(root, dataset, attributelist, tableheader)

    treestack = []
    treestack.append(root)
    treestack.append(100)
    printer(treestack)


if __name__ == "__main__":
    main()


