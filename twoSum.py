class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right =len(numbers) - 1 
        while left <right :
            x = numbers[left] + numbers[right]
            if x == target:
               return(left+1,right+1)
            elif x > target:
                right -= 1
            else:
               left += 1 
        
        
        
