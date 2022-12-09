import math
import copy 
from tabulate import tabulate

class node:

    def __init__(self, dataset, attributelist):
        self.dataset = dataset
        self.attributelist = attributelist
        self.children = []
        self.label = ""



def classifier(root, dataset, attributelist, tableheader):
    classDict = {}

    # print(dataset)
    for i in dataset:
        cValue = i[len(i) - 1]
        if cValue in classDict:
            classDict[cValue] += 1
        else:
            classDict[cValue] = 1

    if len(classDict) == 1 or len(attributelist) == 1:
        return

    # print(classDict)


    samplecount = len(dataset)
    ebf = 0
    for i in classDict:
        p = classDict[i] / samplecount
        ebf += p * math.log(p, 2)
    ebf *= -1

    # print(ebf)



    mgain = 0
    splittingattribute = ""


    for i in attributelist:
        index = tableheader.index(i)
        informationgainforattribute = 0
        atrvar = {}

        for j in dataset:
            atrValue = j[index]
            if atrValue in atrvar:
                atrvar[atrValue] += 1
            else:
                atrvar[atrValue] = 1

        # print(atrvar)

        for k in atrvar:

            datasetPart = [l for l in dataset if l[index] == k]

            # print(datasetPart)
                
            tclassDict = {}

            for m in datasetPart:
                tcValue = m[len(m) - 1]
                if tcValue in tclassDict:
                    tclassDict[tcValue] += 1
                else:
                    tclassDict[tcValue] = 1

            # print(tclassDict)
            
            infogaindj = 0
            tsamplecount = len(datasetPart)

            # print(tsamplecount)

            for n in tclassDict:
                # print("----------",tclassDict[i],"->", tsamplecount)
                p = tclassDict[n] / tsamplecount
                infogaindj += p * math.log(p, 2)
                # print(infogaindj)
            infogaindj *= -1

            # print(infogaindj)


            informationgainforattribute += (atrvar[k] / samplecount) * infogaindj


        # print(informationgainforattribute, "attribute : ", i)

        if ebf - informationgainforattribute > mgain:
            mgain = ebf - informationgainforattribute
            splittingattribute = i
    
    print("splitter:  ",splittingattribute)

    attributelist.remove(splittingattribute)
    index = tableheader.index(splittingattribute)
    # print(index)
    tableheader.pop(index)
    atrvar = {}
    for j in dataset:
        atrValue = j[index]
        if atrValue in atrvar:
            atrvar[atrValue] += 1
        else:
            atrvar[atrValue] = 1

    
    for k in atrvar:
        datasetPart = [l for l in dataset if l[index] == k]    

        for i in datasetPart:
            i.pop(index)

        # print(datasetPart,"--------------")
        tempnode = node(datasetPart, attributelist)
        tempnode.label = k
        root.children.append(tempnode)
        classifier(tempnode, copy.deepcopy(datasetPart), copy.deepcopy(attributelist), copy.deepcopy(tableheader))

    

       
def printer(treestack):

    while(len(treestack) != 0):
        curr = treestack.pop(0)
        if curr == 100:
            print("next level")
            continue

        print(curr.label)
        print(tabulate(curr.dataset, tablefmt="grid"))
        for i in curr.children:
            treestack.append(i)
        treestack.append(100)
    



def main():

    f = open('testdata.txt', 'r')


    attributelist = list(f.readline().strip().split(' '))
    tableheader = list(f.readline().strip().split(' '))
    # print(attributelist)

    lines = f.readlines()
    dataset = []
    for line in lines:
        dataset.append(line.strip().split(' '))

    # print(dataset)
    # attribute_selection_method = input("Enter the choice of attribute selection method ['information gain', 'gain ratio', 'gini index'] : ")
    root = node(dataset, attributelist)
    classifier(root, dataset, attributelist, tableheader)

    treestack = []
    treestack.append(root)
    treestack.append(100)
    printer(treestack)


if __name__ == "__main__":
    main()


