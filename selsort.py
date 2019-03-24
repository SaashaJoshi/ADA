def min_index(arr, low, high):
	if low==high:
		return low
	
	k=min_index(arr, low+1, high)

	if arr[low]<arr[k]:
		return low
	return k

def selsort(arr, low, high):
	if low==high:
		return -1

	k=min_index(arr, low, high)

	if k!=low:
		arr[k], arr[low]=arr[low], arr[k]

	selsort(arr, low+1, high)

if __name__ == '__main__':
	'''
	arr=input('Enter elements: ')
	arr=arr.split()
	'''
	arr=[10, 12, 9, 5, 8, 15, 13]
	n=len(arr)

	selsort(arr, 0, n-1)

	print('Sorted array: ')
	for i in range(n):
		print(arr[i])



