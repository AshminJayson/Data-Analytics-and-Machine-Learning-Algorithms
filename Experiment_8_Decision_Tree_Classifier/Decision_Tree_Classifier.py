class node:
    def __init__(self, dataset, attributelist):
        self.dataset = dataset
        self.attributelist = attributelist
        self.children = []


def classifier_informationgain(root, dataset, attributelist):
    pass


def main():
    f = open('testdata.txt', 'r')

    attributelist = list(f.readline().strip().split(' '))
    # print(attributelist)

    lines = f.readlines()
    dataset = []
    dataset.append(attributelist)
    for line in lines:
        dataset.append(line.strip().split(' '))

    print(dataset)

    # attribute_selection_method = input("Enter the choice of attribute selection method ['information gain', 'gain ratio', 'gini index'] : ")
    root = node(dataset, attributelist)


    classifier_informationgain(root, dataset, attributelist)


if __name__ == "__main__":
    main()

