#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        arr=[]
        for i in str1:
            arr.append(i)
        arr1=arr.copy()
        x=arr[:2]
        i=2
        while i>0:
            arr.pop(0)
            i-=1
        arr=arr+x
        str1="".join(arr)
        if str1==str2:
            return 1
        else:
            a=arr1[-2:]
            i=2
            while i>0:
                arr1.pop()
                i-=1
            arr1=a+arr1
            str1="".join(arr1)
            if str1==str2:
                return 1
            else:
                return 0
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends