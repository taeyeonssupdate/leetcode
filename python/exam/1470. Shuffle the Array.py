class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        x = nums[:n]
        y = nums[n:]
        out = []
        for i in range(n):
            out.append(x[i])
            out.append(y[i])
        return out
