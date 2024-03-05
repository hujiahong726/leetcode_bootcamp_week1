class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myset = set()
        for num in nums:
            if num in myset:
                return True
            else:
                myset.add(num)
        return False