def knapSack(max_capacity, items): 
	n=len(items)
	
	K=[[0 for i in range(max_capacity+1)] for j in range(n+1)]
	
	for i in range(n+1):
		for w in range(max_capacity+1):
			if i==0 or w==0:
				K[i][w]=0
			elif items[i-1][1]<=w:
				K[i][w]=max(items[i-1][0]+K[i-1][w-items[i-1][1]], K[i-1][w])
			else:
				K[i][w]=K[i-1][w]

	return K[n][max_capacity]

if __name__=='__main__':
	'''
	items=input('Enter (value, weight) of the items: ')
	'''

	items=[[60, 10], [100, 20], [120, 30]]	# [value, weight]
	print(items)
	max_capacity=int(input('Enter maximum weight of the knapsack: '))

	print(knapSack(max_capacity, items)) 
	
