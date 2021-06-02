# https://leetcode.com/problems/house-robber-ii/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.straight_rob(nums[1:]), self.straight_rob(nums[:-1]))
        
        
    def straight_rob(self, stash):
        n = len(stash)
        for i in range(2,n):
            if i == 2:
                stash[i] += stash[i-2]
            else:
                stash[i] += max(stash[i-2], stash[i-3])
        return max(stash)
        