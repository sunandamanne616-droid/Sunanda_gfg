class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	j=0
    	for i in range(0,len(arr)):
    	    if arr[i]!=0:
    	        arr[j],arr[i]=arr[i],arr[j]
    	        j+=1
    	return arr