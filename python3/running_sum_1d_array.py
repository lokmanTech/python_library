from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum_array = []
        current_sum = 0
        
        for num in nums:
            current_sum += num
            running_sum_array.append(current_sum)
            
        return running_sum_array
        
# Example usage:
solution =  Solution()
nums1 = [1, 2, 3, 4]
print(solution.runningSum(nums1)) #Output: [1, 3, 6, 10]

nums2 = [1, 1, 1, 1, 1]
print(solution.runningSum(nums2)) #Output: [1, 1, 1, 1, 1]

nums3 = [3, 1, 2, 10, 1]
print(solution.runningSum(nums3)) #Output: [3, 1, 2, 10, 1]

     
