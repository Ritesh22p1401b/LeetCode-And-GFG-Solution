#User function Template for python3
class Solution:
	def sentencePalindrome(self, s):
	    s="".join(s.split())
	    s=s.replace(".","")
	    s=s.replace(";","")
        arr=[]
        for i in s:
            arr.append(i)
        arr1=arr.copy()
        l=len(arr1)
        c=0
        arr.reverse()
        for j in range(l):
            if arr[j]==arr1[j]:
                c+=1
            else:
                c+=0
        if c==l:
            return True
        else:
            return False
	    
		# your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		if ob.sentencePalindrome (s):
			print (1)
		else:
			print (0)
# } Driver Code Ends