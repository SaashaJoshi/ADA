import sys

def minKey(key, mstSet):
	min_key=sys.maxsize		# Default key = infinity

	for i in key:
		if key[i]<min_key and mstSet[i]==False:
			min_key=key[i]
			min_index=i
			print(min_index)

	return min_index

def mstPrims(graph, vertices):
	mstSet=[False]*vertices
	key=[sys.maxsize]*vertices
	parent=[None]*vertices

	key[0]=0
	parent[0]=-1

	for i in range(vertices):
		min_index=minKey(key, mstSet)
		mstSet[min_index]=True

		for v in range(vertices):
			if graph[min_index][v]>0 and key[v]>graph[min_index][v] and mstSet[v]==False:
				key=graph[min_index][v]
				parent[v]=min_index

	return parent



if __name__=='__main__':
	vertices=int(input('Enter the number of vertices in the graph: '))
	graph=input('Enter the graph values: ').split()
	graph=list(graph)
	print(graph)

	parent=mstPrims(graph, vertices)

	print('Parent\t Edge\t Weight')
	for i in range(vertices):
		print('{}\t\t {}\t\t {}\t\t'.format(parent[i], i, graph[parent[i][i]]))


#0,2,3,0,0,0 2,0,5,3,4,0 3,5,0,0,4,0 0,3,0,0,2,3 0,4,4,2,0,5 0,0,0,3,5,0
