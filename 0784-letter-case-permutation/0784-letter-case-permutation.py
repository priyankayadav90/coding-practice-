class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        
        def backtrack(index: int, current: list[str]):
            if index == len(s):
                result.append("".join(current))
                return
            
        
            if s[index].isdigit():
                current.append(s[index])
                backtrack(index + 1, current)
                current.pop()
            else:
            
                current.append(s[index].lower())
                backtrack(index + 1, current)
                current.pop()
                
            
                current.append(s[index].upper())
                backtrack(index + 1, current)
                current.pop()

        backtrack(0, [])
        return result
