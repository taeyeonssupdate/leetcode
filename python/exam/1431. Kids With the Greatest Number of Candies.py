class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        _max = max(candies)
        return [True if candy >= _max else False for candy in list(map(lambda x:x+extraCandies, candies))]

x = Solution()
print(x.kidsWithCandies([2, 3, 5, 1, 3], 3))

