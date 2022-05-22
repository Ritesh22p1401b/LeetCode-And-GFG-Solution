#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        if len(a)!=len(b):
            return False
        else:
            l=[0]*256
            for i in range(len(a)):
                l[ord(a[i])]+=1
                l[ord(b[i])]-=1
            if l==[0]*256:
                return True
            else:
                return False
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends