class Solution:
    def createTargetArray(self, nums, indexs):
        x=[]
        for i in range(len(nums)):
            x.insert(indexs[i],nums[i])
        return x


#把num插入在index的位置
print(Solution().createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
