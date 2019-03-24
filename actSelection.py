def actSelection(start, finish):
	n=len(start)
	i=0
	activity=[i]
	
	for j in range(1, n):
		if start[j]>=finish[i]:
			activity.append(j)
			i=j	

	return activity	

if __name__=='__main__':
	act=input('Enter (si, fi) of activities (sorted): ').split()		# Sorted accord to finish time
	start=[]
	finish=[]
	
	for i in act:
		(s, f)=tuple(map(int, i.split(',')))
		start.append(s)
		finish.append(f)
	'''
	start.append(input('Enter start time of activities: ').split())
	finish.append(input('Enter finish time of activities: ').split())	
	'''
	activity=actSelection(start, finish)
	print(activity)