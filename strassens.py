def mDimension(matrix):
	return len(matrix), len(matrix[0])

def defaultMult(matrix_a, matrix_b):
	newMatrix=[[matrix_a[0][0]*matrix_b[0][0] + matrix_a[0][1]*matrix_b[1][0] , matrix_a[0][0]*matrix_b[0][1] + matrix_a[0][1]*matrix_b[1][1]], [matrix_a[1][0]*matrix_b[0][0] + matrix_a[1][1]*matrix_b[1][0] , matrix_a[1][0]*matrix_b[0][1] + matrix_a[1][1]*matrix_b[1][1]]]
	return newMatrix

def mAddition(matrix_a, matrix_b):
	return [[matrix_a[r][c]+matrix_b[r][c] for c in range(len(matrix_a[r]))] for r in range(len(matrix_a))]

def mSubtraction(matrix_a, matrix_b):
	return [[matrix_a[r][c]-matrix_b[r][c] for c in range(len(matrix_a[r]))] for r in range(len(matrix_a))]

def mSplit(matrix):
	n=len(matrix)

	if len(matrix)%2!=0 or len(matrix[0])%2!=0:
		raise Exception('Odd dimensional matrices are not supported.')

	mid=int(n/2)

	tLeft=[[matrix[i][j] for j in range(mid)] for i in range(mid)]
	tRight=[[matrix[i][j] for j in range(mid, n)] for i in range(mid)]

	bLeft=[[matrix[i][j] for j in range(mid)] for i in range(mid, n)]
	bRight=[[matrix[i][j] for j in range(mid, n)] for i in range(mid, n)]

	return tLeft, tRight, bLeft, bRight

def strassen(matrix_a, matrix_b):
	if mDimension(matrix_a)!=mDimension(matrix_b):
		raise Exception('Both matrices are not of same dimensions.')

	if mDimension(matrix_a)==(2, 2):
		return defaultMult(matrix_a, matrix_b)

	A, B, C, D=mSplit(matrix_a)
	E, F, G, H=mSplit(matrix_b)

	p1=strassen(A, mSubtraction(F, H))
	p2=strassen(mAddition(A, B), H)
	p3=strassen(mAddition(C, D), E)
	p4=strassen(D, mSubtraction(G, E))
	p5=strassen(mAddition(A, D), mAddition(E, H))
	p6=strassen(mSubtraction(B, D), mAddition(G, H))
	p7=strassen(mSubtraction(A, C), mAddition(E, F))

	tLeft=mAddition(mSubtraction(mAddition(p4, p5), p2), p6)
	tRight=mAddition(p1, p2)

	bLeft=mAddition(p3, p4)
	bRight=mSubtraction(mSubtraction(mAddition(p1, p5), p3), p7)

	newMatrix=[]

	for i in range(len(tRight)):
		newMatrix.append(tLeft[i]+tRight[i])
	for i in range(len(bRight)):
		newMatrix.append(bLeft[i]+bRight[i])

	return newMatrix

if __name__=='__main__':
	matrix_a=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
	matrix_b=[[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]

	newMatrix=strassen(matrix_a, matrix_b)
	print(newMatrix)
