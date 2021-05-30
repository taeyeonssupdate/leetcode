class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        _max = 0
        for user in accounts:
            if sum(user) >_max:
                _max = sum(user)
        return _max
