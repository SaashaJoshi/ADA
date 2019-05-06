def longestSubSeq(seq1, seq2):
	n1=len(seq1)
	n2=len(seq2)

	LongestSeq=[[None]*(n2+1) for i in range(n1+1)]

	for i in range(n1+1):
		for j in range(n2+1):
			if i==0 or j==0:
				LongestSeq[i][j]=0
			elif seq1[i-1]==seq2[j-1]:
				LongestSeq[i][j]=LongestSeq[i-1][j-1]+1
			else:
				LongestSeq[i][j]=max(LongestSeq[i-1][j], LongestSeq[i][j-1])

	return LongestSeq[n1][n2]


if __name__=='__main__':
	'''
	seq1=input('Enter first sequence: ')
	seq2=input('Enter second sequence: ')
	'''
	seq1='AGGTAB'
	seq2='GXTXAYB'
	print('Length of Longest Subsequence is: ', longestSubSeq(seq1, seq2))