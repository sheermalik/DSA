class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        left,right=0,len(nums)-1
        mid = (left+right) //2
        result=nums[mid]

        while left<  right :
            mid = (left+right) //2
            result=min(nums[mid],result)
            if nums[left] < nums[right]:
                result=min (result, nums[left])
                break

            if nums[mid] >= nums[left]:
                left=mid+1
                result= min(nums[mid],result)
            else:
                right=mid-1
                result= min(nums[mid],result)
        #result=min (result, nums[left])    
        return min(result, nums[left])
   

