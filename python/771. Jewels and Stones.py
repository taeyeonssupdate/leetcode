"""
http://cvfiasd.pixnet.net/blog/post/279015652-leetcode%23771-jewels-and-stones
該題Jewels and Stones的題目如下所示，想要從S矩陣中找出有幾個J矩陣的元素
範例1中，有一個J矩陣中有a以及A的元素，在給定一個S矩陣，該例子中，S矩陣中共有1個a以及2個A
因此輸出為3，範例2中，J矩陣的元素為z，而S矩陣的元素為Z，S矩陣中完全沒有包含J矩陣的元素，因此輸出為0。
"""


class Solution:
    def numJewelsInStones(self, J, S):
        setJ = set(J)
        return sum(s in setJ for s in S)
