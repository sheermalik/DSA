class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        DuplicateSet = set()

        for i in nums:
            if i in DuplicateSet:
                return True
            else:
                DuplicateSet.add(i)

        return False        
