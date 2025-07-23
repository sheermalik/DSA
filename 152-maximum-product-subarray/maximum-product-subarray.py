class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=  nums[0]
        currentMin,currentMax=1,1

        for n in nums:
            var_max=n*currentMax
            currentMax=max(var_max, n*currentMin, n)
            currentMin= min (var_max,n*currentMin, n)
            result= max(currentMax,result)

        return result    

