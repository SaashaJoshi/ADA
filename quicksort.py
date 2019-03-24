def partition(arr, low, high):
	pos=low
	pivot=arr[high]

	for i in range(low, high):
		if arr[i]<pivot:
			arr[pos], arr[i]=arr[i], arr[pos]
			pos+=1
	arr[pos], arr[high]=arr[high], arr[pos]
	return pos

def quicksort(arr, low, high):
	if low<high:
		pos=partition(arr, low, high)

		quicksort(arr, low, pos-1)
		quicksort(arr, pos+1, high)

if __name__=='__main__':
	'''
	arr=input('Enter elements: ')
	arr=arr.split()
	'''
	arr=[10, 12, 9, 5, 8, 15, 13]
	n=len(arr)

	quicksort(arr, 0, n-1)

	print('Sorted array: ')
	for i in range(n):
		print(arr[i])
