class Solution(object):
    def singleNumber(self, nums):
        return sum(list(set(nums)))*2 - sum(nums)

    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key

    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
        
    def singleNumber3(self, nums):
        print(nums)
        print(set(nums))
        print(sum(nums))
        print(sum(set(nums)))
        print(sum(set(nums))*2)
        return 2*sum(set(nums))-sum(nums)
        
    #python 2,7
    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
        
    #python 2,7
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)


#超時8064毫秒
class mySolution:
    def singleNumber(self, nums):
        return [i for i in nums if nums.count(i) == 1][0]


print(Solution().singleNumber3([2, 2, 1]))
