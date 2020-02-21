class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        print(s, id(s))
        s.reversed
        s=s[::-1]
        print(s, id(s))

Solution().reverseString(["h", "e", "l", "l", "o"])
