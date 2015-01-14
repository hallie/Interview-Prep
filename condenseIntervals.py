'''
Four-part program.
The person asking this question had me write a function that returned
    True/False if two input intervals overlapped.
Then a function that merged two overlapping intervals.
Then a fuction that uses both of the previous functions to condense a list of
    intervals by merging all of the overlapping ones.
I also added a function that takes a list of numbers and creates an interval
    by finding the biggest and the smallest number.
'''
allDaNums = [[1,2,3,4,5,6,7,8,9],[5,3,2,5,7,8,10,13],
             [11,42,82],[99,100],[876,432,234], [200,400]]

#make intervals
def doTheDoo(allDaNums):
	i = 0
	while i < len(allDaNums):
		interval = allDaNums[i]
		low = interval[0]
		high = interval[0]
		for num in interval:
			if num < low:
				low = num
			if num > high:
				high = num
		allDaNums[i] = [low,high]
		i+=1
	return allDaNums
#print "\nMake Intervals:"
#print doTheDoo(allDaNums)
# [[1, 9], [2, 13], [11, 82], [99, 100], [234, 876], [200, 400]]
		
#does overlap
def doesOverlap(A,B):
	if A[0] <= B[0] <= A[1] or A[0] <= B[1] <= A[1]:
		return True
	else:
		return False
#print "\nDoes Overlap:"
#m = doTheDoo(allDaNums)
#A = m[0]
#B = m[1]
#print doesOverlap(A,B)
# True

#merge intervals
def doMerger(A,B):
	if doesOverlap(A,B):
		if A[0] < B[0]:
			low = A[0]
		else:
			low = B[0]
		if A[1] > B[1]:
			high = A[1]
		else:
			high = B[1]
		return low,high
	else:
		print "Does not overlap. Will not merge."
#print "\nDo Merger:"
#print doMerger(A,B)
# (1,13)
		
#condence list of intervals
def condenceList(listOLists):
	intervals = doTheDoo(listOLists)
	i = 0
	while i < len(intervals):
		A = intervals[i]
		j = i+1
		while j < len(intervals):
			B = intervals[j]
			if doesOverlap(A,B):
				A = doMerger(A,B)
				intervals[i] = A
				intervals.pop(j)
			else:
				j+=1
		i+=1
	return intervals
#print "\nCondenced List of Intervals:"
#print condenceList(allDaNums)
# [(1, 82), [99, 100], (200, 876)]
