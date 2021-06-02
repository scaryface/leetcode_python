# https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, stash):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(stash)
        #stash = [nums[i] for i in range(n)]
        for i in range(2,n):
            if i == 2:
                stash[i] += stash[i-2]
            else:
                stash[i] += max(stash[i-2], stash[i-3])
        return max(stash)
        
