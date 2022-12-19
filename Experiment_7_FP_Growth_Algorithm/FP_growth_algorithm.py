from tabulate import tabulate
from itertools import combinations

class node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.count = 1
        self.children = []
        self.prefixstr = ""


def createFPTree(root, data, i=0):

    if i == len(data):
        return

    for child in root.children:
        if data[i] == child.value:
            child.count += 1
            createFPTree(child, data, i+1)
            return

    temp = node(data[i], root)
    if root.value == 'null':
        temp.prefixstr = ''
    elif root.prefixstr == '':
        temp.prefixstr = root.value
    else:
        temp.prefixstr = root.prefixstr + ',' + root.value

    root.children.append(temp)
    createFPTree(temp, data, i+1)


def printTree(root, markerStr="+- ", levelMarkers=[]):

    # Credits to : https://simonhessner.de/python-3-recursively-print-structured-tree-including-hierarchy-markers-using-depth-first-search/ for this function

    emptyStr = " "*len(markerStr)
    connectionStr = "|" + emptyStr[:-1]
    level = len(levelMarkers) 
    
    mapper = lambda draw: connectionStr if draw else emptyStr
    markers = "".join(map(mapper, levelMarkers[:-1]))
    markers += markerStr if level > 0 else ""
    print(f"{markers}{root.value}{':'}{root.count}")
    # print(f"{markers}{root.value}{':'}{root.count}{'->'}{root.prefixstr}")


    for i, child in enumerate(root.children):
        isLast = i == len(root.children) - 1
        printTree(child, markerStr, [*levelMarkers, not isLast])





def miningConditionalPatternBase(root, FPTable):
    if root == None:
        return
    
    noOfChildren = len(root.children)

    
    for i in range(noOfChildren - 1):
        miningConditionalPatternBase(root.children[i], FPTable)

    flag = 0
    for itemdata in FPTable:
        if itemdata[0] == root.value and root.prefixstr != '':
            itemdata[1].append(root.prefixstr + ':' + str(root.count))
            flag = 1

    if flag == 0 and root.value != 'null' and root.prefixstr != '':
        FPTable.append([root.value, [root.prefixstr + ':' + str(root.count)], [], []])

    if noOfChildren > 0:
        miningConditionalPatternBase(root.children[noOfChildren - 1], FPTable)




def createConditionalFPTree(FPTable, min_sup):
    # for row in FPTable:
    #     if row[0] == 'Item':
    #         continue
        
    #     conditionFPTree = {}    
    #     for base in row[1]:
    #         firstsplit = base.split(':')
    #         secondsplit = firstsplit[0].split(',')
            
    #         for item in secondsplit:
    #             if item in conditionFPTree:
    #                 conditionFPTree[item] += int(firstsplit[1])
    #             else:
    #                 conditionFPTree[item] = int(firstsplit[1])

    #     for key in conditionFPTree.copy():
    #         if conditionFPTree[key] < min_sup:
    #             conditionFPTree.pop(key)

    #     row[2] = conditionFPTree

    for itemset in FPTable[1:]:
        conditionalRootNode = node('null', None)
        for base in itemset[1]:
            firstsplit = base.split(':')
            secondsplit = firstsplit[0].split(',')
            for i in range(int(firstsplit[1])):
                createFPTree(conditionalRootNode, secondsplit)
        printTree(conditionalRootNode)
        leaflist = []


def miningConditionalPatternFPTree(root, leaflist):
    if root == None:
        return
    
    noOfChildren = len(root.children)

    for i in range(noOfChildren - 1):
        miningConditionalPatternFPTree(root.children[i], leaflist)

    

    if noOfChildren > 0:
        miningConditionalPatternFPTree(root.children[noOfChildren - 1], leaflist)




def generateFrequentPatterns(FPTable):
    for row in FPTable:
        if row[0] == 'Item':
            continue
        Fpatterns = {}
        for length in range(1,len(row[2]) + 1):
            for x in combinations(row[2], length):
                minval = 1000000
                # print(list(x))
                key = ''
                for y in list(x):
                    if row[2][y] < minval:
                        minval = row[2][y]
                    key += y
                Fpatterns[key + row[0]] = minval

        row[3] = Fpatterns
            
        



def main(): 

    #Reading data from dataset
    transactions = {}

    f = open('./dataset.txt', 'r')
    lines = f.readlines()

    for line in lines:
        data = line.strip().split(' ')
        transactions[data[0]] = data[1:]


    #Counting one item frequent sets
    c1 = {}
    for key in transactions:
        transactions[key] = sorted(list(set(transactions[key])))
        for item in transactions[key]:
            if item in c1:
                c1[item] += 1
            else: 
                c1[item] = 1

    min_sup = int(input("Enter the minimum support value : "))
    #Sorting each transaction based on c1
    for key in transactions:
        transactions[key] = sorted(transactions[key], key = lambda x : c1[x], reverse=True)
        transactions[key] = [i for i in transactions[key] if c1[i] >= min_sup]

    print("\n\nDataset")
    print(tabulate(transactions, headers=transactions.keys(), tablefmt='outline'))
    c1list = list(c1.items())
    c1list.insert(0, ('Item', 'Sup_count'))
    print("\n\n Frequency Table")
    print(tabulate(c1list, headers="firstrow", tablefmt='outline'))
    root = node('null', None)


    #Create and print FP Tree
    for key in transactions:
        createFPTree(root, transactions[key])
    
    print("\n--------------------> FP TREE <--------------------")
    printTree(root)

    #Create table and find frequent patterns
    FPTable = [['Item', 'Conditional Pattern Base', 'Conditional FP Tree', 'Frequent Pattern Generated']]
    miningConditionalPatternBase(root, FPTable)
    FPTable[1:] = sorted(FPTable[1:], key = lambda x : x[0])
    # print(FPTable)

    createConditionalFPTree(FPTable, min_sup)

    generateFrequentPatterns(FPTable)
    print("\n\nPattern Generation Table")
    print(tabulate(FPTable, headers="firstrow", tablefmt='outline'))

if __name__ == '__main__':
    main()