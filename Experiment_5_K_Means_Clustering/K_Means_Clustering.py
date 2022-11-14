from random import randint
from tabulate import tabulate

def euclideandist(a, b):
	dist = 0
	for ind in range(len(a)):
		dist += (a[ind] - b[ind]) ** 2
	return (dist ** 0.5)

def printer(dp, centroids, clusterlist, dists):
	line = '-' * (len(centroids) + 1) * 15
	print(line)
	print("|{:^13}|".format("-"), end = ' ')
	for i in centroids : 
		print("{:^12} |".format(str(i)), end = ' ')
	print()
	for i in range(len(dp)):
		print("|{:^13}|".format(str(dp[i])), end = ' ')
		for j in range(len(centroids)):
			print("{:^12} |".format(str(dists[i][j])), end = ' ')
		print()
	print(line)
f = open('./dataset.txt', 'r')

lines = f.readlines()
dp = []
for line in lines:
	dp.append(list(map(int, line.split(','))))

num_of_dp = len(dp)
num_of_attr = len(dp[0])

k = randint(2, num_of_dp - 1)
print("The randomly chosen number of clusters is : ", k)

centroids = []

while len(centroids) != k:
	temp = randint(0, num_of_dp - 1)
	
	if dp[temp] not in centroids:
		centroids.append(dp[temp])

print("The randomly chosen centroids are : ", centroids)

clusterlist = [-1] * len(dp)
check = True
itercount = 1
while check:
	check = False
	
	dists = []
	for pno, p in enumerate(dp):
		closestcentroid, valclosestcentroid = -1, 100000
		tdist = [] 
		for i, cent in enumerate(centroids):
			dist = euclideandist(p, cent)
			tdist.append(round(dist, 2))
			
			if dist < valclosestcentroid :
				valclosestcentroid = dist
				closestcentroid = i
			
		if clusterlist[pno] != closestcentroid:
			check = True
			clusterlist[pno] = closestcentroid
		dists.append(tdist)
	
	print("\n\nIteration : ", itercount)
	itercount += 1
	printer(dp, centroids, clusterlist, dists)
	for ind in range(len(centroids)):
		mean, count = [0] * num_of_attr, 0
		
		for p, clust in enumerate(clusterlist):
			if clust == ind:
				count += 1
				for i in range(num_of_attr):
					mean[i] += dp[p][i]
					
		for i in range(num_of_attr):
			mean[i] /= count
			
		mean = [round(i, 2) for i in mean]
		centroids[ind] = mean
		
		


		



