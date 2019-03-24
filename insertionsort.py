def insertionsort(arr, high):
	if high<=1:
		return arr

	insertionsort(arr, high-1)

	last=arr[high-1]
	j=high-2

	while j>=0 and arr[j]>last:
		arr[j+1]=arr[j]
		j-=1

	arr[j+1]=last

if __name__=='__main__':
	'''
	arr=input('Enter elements: ')
	arr=arr.split()
	'''
	arr=[10, 12, 9, 5, 8, 15, 13]
	n=len(arr)

	insertionsort(arr, n)

	print('Sorted array: ')
	for i in range(n):
		print(arr[i])

