class Solution:
    def fizzBuzz(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

class mySolution:
    def fizzBuzz(self, n):
        data = [str(i) for i in range(1,n+1)]
        for i in range(n):
            if not int(data[i]) % 3 and not int(data[i]) % 5:
                data[i] = 'FizzBuzz'
            elif not int(data[i]) % 3:
                data[i] = 'Fizz'
            elif not int(data[i]) % 5:
                data[i] = 'Buzz'
        return data

import json
print(json.dumps(Solution().fizzBuzz(15),indent= 4, ensure_ascii=False))
