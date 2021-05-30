class Solution:
    def isValid(self, s):
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
        return not len(s)


#用replace抽出來
text = "{}[]()"
print(Solution().isValid(text))
