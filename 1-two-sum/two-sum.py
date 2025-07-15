class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap= {}

        for i,value in enumerate(nums):
            difference= target-value
            if difference in myMap:
                return [myMap[difference],i]

            myMap[value]=i    

        return    