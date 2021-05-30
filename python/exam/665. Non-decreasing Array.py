class Solution:
    def checkPossibility(self, nums):
        x = 0
        cache_num = nums[0]
        for i in range(1, len(nums)-1):
            print(cache_num)
            if cache_num > nums[i]:
                x += 1
            cache_num = nums[i]
        print(x)
        if x > 1:
            return False
        return True


print(Solution().checkPossibility([4, 2, 3]))
print(Solution().checkPossibility([4, 2, 1]))
print(Solution().checkPossibility([-1, 4, 2, 3]))
print(Solution().checkPossibility([3, 4, 2, 3]))
