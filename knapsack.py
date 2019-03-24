def fracKanpsack(value, weight, order):
	max_capacity=int(input('Enter maximum weight of the knapsack: '))
	max_value=0
	knapsack=[]
	fraction=[0]*len(value)

	for i in order:
		if weight[i]<=max_capacity:
			fraction[i]=1
			max_capacity-=weight[i]
			max_value+=value[i]
			knapsack.append(i)
		else:
			fraction[i]=max_capacity/weight[i]
			max_value+=value[i]*fraction[i]
			knapsack.append(i)
			break

	print('Knapsack Items: ', knapsack)
	print('Maximum Value: ', max_value)
	print('Fraction of items in knapsack: ', fraction)

def findOrder(value, weight):
	pair=zip(value, weight)
	order=list(range(len(value)))
	ratio=[]

	for (v, w) in pair:
		ratio.append(v/w)

	order.sort(key= lambda i:ratio[i], reverse=True)

	return order

if __name__=='__main__':
	items=input('Enter (value, weight) of the items: ').split()
	value=[]
	weight=[]

	for i in items:
		(v, w)=tuple(map(int, i.split(',')))
		value.append(v)
		weight.append(w)

	order=findOrder(value, weight)
	fracKanpsack(value, weight, order)
