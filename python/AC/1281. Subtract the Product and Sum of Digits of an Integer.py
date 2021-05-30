class Solution:
    def subtractProductAndSum(self, n):
        A = map(int, str(n))
        return reduce(operator.mul, A) - sum(A)


class mySolution:
    def subtractProductAndSum(self, n: int) -> int:
        return eval(str(n).replace('', '*')[1:-1])-eval(str(n).replace('', '+')[1:-1])



print(Solution().subtractProductAndSum(234))
