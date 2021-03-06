class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        answer = 0
        
        a = 0
        b = len(height)-1
        
        while a < b:
            h = min(height[a], height[b])
            w = (b-a)
            tmp =  w * h 
            answer = max(answer, tmp)
            
            if height[a] <= height[b]:
                a += 1
            
            else: #height[a] > height[b]
                b -= 1
        
        return answer