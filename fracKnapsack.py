def fracKanpsack(items):
	max_capacity=int(input('Enter maximum weight of the knapsack: '))
	max_value=0
	knapsack=[]
	fraction=[0]*len(items)

	for i in range(len(items)):
		if items[i][1]<=max_capacity:
			fraction[i]=1
			max_capacity-=items[i][1]
			max_value+=items[i][0]
			knapsack.append(i)
		else:
			fraction[i]=max_capacity/items[i][1]
			max_value+=items[i][0]*fraction[i]
			knapsack.append(i)
			break

	print('Knapsack Items: ', knapsack)
	print('Maximum Value: ', max_value)
	print('Fraction of items in knapsack: ', fraction)

def findOrder(items):
	#pair=zip(value, weight)
	ratio=[items[i][0]/items[i][1] for i in range(len(items))]
	items.sort(key= lambda items:ratio[0], reverse=True)
	print(items)

	return items

if __name__=='__main__':
	'''
	items=input('Enter (value, weight) of the items: ')
	
	value=[]
	weight=[]

	for i in items:
		(v, w)=tuple(map(int, i.split(',')))
		value.append(v)
		weight.append(w)
	'''

	items=[[60, 10], [100, 20], [120, 30]]	# [value, weight]
	items=findOrder(items)
	fracKanpsack(items)
