from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        total_subarrays = 0
        running_prefix_sum = 0
        
        
        remainder_counts = defaultdict(int)
        remainder_counts[0] = 1
        
        for num in nums:
    
            running_prefix_sum += num
            
        
            remainder = running_prefix_sum % k
            

            if remainder in remainder_counts:
                total_subarrays += remainder_counts[remainder]
            
            remainder_counts[remainder] += 1
            
        return total_subarrays
