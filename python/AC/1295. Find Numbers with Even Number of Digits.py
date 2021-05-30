class Solution:
    def findNumbers(self, nums):
        # n=0
        # for num in nums:
            # if not len(str(num)) % 2:
                # n+=1
        return sum(not len(str(num)) % 2 for num in nums)


print(Solution().findNumbers([555, 901, 482, 1771]))
nums = [555, 901, 482, 1771]
qwe = [x for x in (not len(str(num)) % 2 for num in nums if num != 1771)]
print(qwe)