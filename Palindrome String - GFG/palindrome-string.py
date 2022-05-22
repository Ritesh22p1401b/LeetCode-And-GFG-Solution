#User function Template for python3
class Solution:
	def isPalindrome(self, S):
	    s1=""
	    for i in S:
	        s1=s1+i+" "
	    l=s1.split()
	    l.reverse()
	    s1="".join(l)
	    if S==s1:
	        return 1
	    else:
	        return 0
        
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends