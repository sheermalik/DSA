class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        left,right=0,len(nums)-1
        result=nums[0]
        while left<  right :
            mid = (left+right) //2
            result=min(nums[mid],result)
            if nums[left] < nums[right]:
                
                break

            if nums[mid] >= nums[left]:
                left=mid+1
             
            else:
                right=mid-1
               
        #result=min (result, nums[left])    
        return min(result, nums[left])
   

