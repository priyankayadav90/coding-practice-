class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        
        def dfs(path: str):
            if len(path) == n:
                ans.append(path)
                return
            if path and path[-1] == '0':
                dfs(path + '1')
            else:
                dfs(path + '0')
                dfs(path + '1')
                
        dfs("")
        return ans
