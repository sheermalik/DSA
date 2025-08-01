class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right= 0, len(numbers)-1

        while left < right:
            sum=numbers[left]+numbers[right]

            if target> sum:
                left+=1
            elif target < sum:
                right-=1
            else:
                return (left+1,right+1)    
        return []        