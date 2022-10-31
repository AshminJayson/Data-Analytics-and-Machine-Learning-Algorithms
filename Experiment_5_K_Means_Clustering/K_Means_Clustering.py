# Warning Unverified

from random import randint
from tabulate import tabulate


#Function for calculating euclidean distance
def euclideandist(a, b) :
    dist = 0
    for ind in range(len(a)):
        dist += (a[ind] - b[ind]) ** 2
    
    return (dist ** 0.5)


f = open('./dataset.txt', 'r')

lines = f.readlines()

dp = []
for line in lines:
    dp.append(list(map(int, line.split(','))))

num_of_dp = len(dp)
num_of_attr = len(dp[0])

#Random selection of cluster number
k = randint(2, num_of_dp - 1)
print("The number of chosen clusters is : ", k)

centroids = []

#Random selection of centroids
while len(centroids) != k :
    temp = randint(0, num_of_dp - 1)

    if dp[temp] not in centroids : 
        centroids.append(dp[temp])

print("The randomly chosen centroids are : ", centroids)

clusterlist = [-1] * len(dp)
check = True

#Iterative clustering
while check :
    check = False

    #Calculation of closest cluster
    for pno, p in enumerate(dp):
        closestcentroid, valclosestcentroid = -1, 100000000
        for i, cent in enumerate(centroids):
            dist = euclideandist(p, cent)
            if dist < valclosestcentroid:
                valclosestcentroid = dist
                closestcentroid = i

        if clusterlist[pno] != closestcentroid:
            check = True
            clusterlist[pno] = closestcentroid


    #Calculation of new centroid
    for ind in range(len(centroids)):
        mean, count = [0] * num_of_attr, 0

        for p, clust in enumerate(clusterlist):
            if clust == ind:
                count += 1
                for i in range(num_of_attr):
                    mean[i] += dp[p][i]
        for i in range(num_of_attr):
            mean[i] /= num_of_attr
        mean = [round(i, 2) for i in mean]
        centroids[ind] = mean



#Output section to be done later
            

