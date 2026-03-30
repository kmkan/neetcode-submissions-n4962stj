class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        i = len(heights) - 1

        buildings = []
        while i >= 0:
            if heights[i] > max_height:
                buildings.append(i)
                max_height = max(max_height, heights[i])
            i -= 1
        
        buildings.reverse()

        return buildings