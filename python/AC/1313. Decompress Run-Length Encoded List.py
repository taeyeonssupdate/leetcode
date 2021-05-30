class Solution:
    def decompressRLElist(self, nums):
        return [x for a, b in zip(nums[0::2], nums[1::2]) for x in [b] * a]


class Solution2:
    def decompressRLElist(self, nums):
        asw = []
        for a, b in zip(nums[0::2], nums[1::2]):
            for x in [b] * a:
                asw.append(x)
        return asw





print(Solution2().decompressRLElist([1,2,3,4]))
