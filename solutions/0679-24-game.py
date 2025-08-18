class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums):
            n = len(nums)
            if n == 1:
                return abs(nums[0] - 24.0) < EPS
            
            for i in range(n - 1):
                for j in range(i + 1, n):
                    a, b = nums[i], nums[j]
                    candidates = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)
                    
                    remaining_nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                    for val in candidates:
                        if dfs(remaining_nums + [val]):
                            return True
            return False
        
        return dfs(cards) 