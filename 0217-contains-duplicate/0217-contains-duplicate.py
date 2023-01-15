class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        diff = set()
        for i in nums:
            if i in diff:
                return True
            else:
                diff.add (i)

