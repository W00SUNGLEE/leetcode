class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        def dfs(sr: int, sc: int, newColor: int):
            oldColor = image[sr][sc]
            image[sr][sc] = newColor
        
        
            if sr > 0:
                if image[sr-1][sc] == oldColor:
                    dfs(sr-1, sc, newColor)
        
            if sr < len(image) - 1:
                if image[sr+1][sc] == oldColor:
                    dfs(sr+1, sc, newColor)
        
            if sc > 0 :
                if image[sr][sc-1] == oldColor:
                    dfs(sr, sc-1, newColor)
        
            if sc < len(image[0]) - 1:
                if image[sr][sc+1] == oldColor:
                    dfs(sr, sc+1, newColor)
        
        dfs(sr, sc, newColor)
        
        return image    