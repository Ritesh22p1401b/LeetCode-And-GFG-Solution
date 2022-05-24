#User function Template for python3


class Solution:
    def countWords(self,List, n):
        d = {}
        c = 0
        for i in List:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for keys, value in d.items():
            if value == 2:
                c += 1
        return c
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        List = input().split()
        ob = Solution()
        print(ob.countWords(List, n))
# } Driver Code Ends