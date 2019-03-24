def minMax(arr, low, high):
	mid=int((low+high)/2)
	length=high-low

	if length==1:
		return (arr[0], arr[0])

	elif length==2:
		return (min(arr), max(arr))

	elif length>2:
		(min1, max1)=minMax(arr, low, mid)
		(min2, max2)=minMax(arr, mid+1, high)

	return (min(min1, min2), max(max1, max2))

if __name__=='__main__':
	'''
	arr=input('Enter elements: ')
	arr=arr.split()
	'''
	arr=[10, 12, 9, 5, 8, 15, 13]
	n=len(arr)

	(min, max)=minMax(arr, 0, n-1)

	print('Max element is: ', max)
	print('Min element is: ', min)
