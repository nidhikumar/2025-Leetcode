class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * (len(height))
        max_right = [0] * (len(height))
        min_array = [0] * (len(height))
        max_left[0] = 0
        max_right[len(height)-1] = 0
        storedWater = 0
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        for i in range(len(max_left)):
            min_array[i] = min(max_left[i], max_right[i])
        for i in range(len(min_array)):
            storedWater += (min_array[i] - height[i]) if (min_array[i] - height[i]) >= 0 else 0
        # print(height)
        # print(max_left[0:len(height)])
        # print(max_right[0:len(height)])
        # print(min_array[0:len(height)])
        return storedWater