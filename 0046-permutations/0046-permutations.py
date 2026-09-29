class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(current_path, visited):
            
            if len(current_path) == len(nums):
                res.append(current_path.copy()) 
                return
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    current_path.append(num)
                    
                    backtrack(current_path, visited)
                    
                    
                    current_path.pop()
                    visited.remove(num)
                    
        backtrack([], set())
        return res
