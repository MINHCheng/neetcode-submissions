class Solution:
    def trap(self, height: List[int]) -> int:
        left : int = 0
        right : int = len(height)-1
        left_max = left
        right_max = right
        rain_water = 0

        test = []

        while(left <= right):
            if height[left_max] <= height[right_max]:
                rain = height[left_max] - height[left]
                if rain < 0:
                    rain = 0
                    left_max = left
                left+=1
            else:
                rain = height[right_max] - height[right]
                if rain < 0:
                    rain = 0
                    right_max = right
                right -= 1
            test.append(rain)
            rain_water += rain
        print(test)
        return rain_water


        