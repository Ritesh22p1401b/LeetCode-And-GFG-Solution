#User function Template for python3
class Solution:
	def removeDups(self, S):
	    a=S
	    S=""
	    for i in a:
	        if i not in S:
	            S+=i
	    return S
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends