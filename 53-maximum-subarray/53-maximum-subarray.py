import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize -1
        current_sum = 0
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
            
        return best_sum


"""
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize -1
        #best_start = 0
        #best_end = 0
        current_sum = 0
        
        for current_end, x in enumerate(nums):
            if current_sum <= 0:
                current_start = current_end
                current_sum = x
            else:
                current_sum += x
            
            if current_sum > best_sum:
                best_sum = current_sum
                #best_start = current_start
                #best_end = current_end + 1
                
            print(best_sum)
        return best_sum
"""