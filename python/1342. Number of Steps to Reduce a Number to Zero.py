class Solution:
    def numberOfSteps(self, num):
        n = 0
        while num:
            if num%2 == 0:
                n+=1
                num/=2
            elif num%2 != 0:
                n+=1
                num-=1
        return n


class Solution2:
    def numberOfSteps(self, num: int) -> int:
        print(f'{num:b}')
        digits = f'{num:b}'
        print(len(digits))
        return digits.count('1') - 1 + len(digits)

print(Solution().numberOfSteps(14))