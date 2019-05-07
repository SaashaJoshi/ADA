import sys

def NQueens(queen, n, arr):
	for i in range(n):
		if Place(queen, i, arr):
			arr.append(i)
			print(arr)
			if queen==n-1:
				for k in range(n):
					print(k+','+arr[k])
			NQueens(queen+1, n, arr)

def Place(queen, i, arr):
	for j in range(queen):
		if arr[j]==i or abs(arr[j]-i)==abs(queen-j):
			return False
	return True

if __name__=='__main__':
	n=int(input('Enter dimensions of the chess board: '))
	arr=[]
	NQueens(0, n, arr)
