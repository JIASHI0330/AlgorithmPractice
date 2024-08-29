"""
Questions to ask the interview to verify the constraints

1. Do the left and right sides of the graph count as walls

2. Will there be negative integers

Test cases:
[0,1,0,2,1,0,1,3,2,1,2,1]    return 6
[]                           return 0
[3]                          return 0
[3, 4, 3]                    return 0
"""


#
# def trap(height):
#     total_area = 0
#     for i in range(1, len(height) - 1):
#         curr_height = height[i]
#         lMax = max(height[0:i])
#         rMax = max(height[i + 1:])
#         curr_water = min(lMax, rMax) - curr_height
#         if curr_water < 0:
#             curr_water = 0
#         total_area += curr_water
#
#     return total_area

def trap(height):
    total_area = 0
    lMax = 0
    rMax = len(height) - 1
    maxLeft = 0
    maxRight = 0
    while lMax < rMax:
        if height[lMax] <= height[rMax]:
            if height[lMax] > maxLeft:
                maxLeft = height[lMax]
            curr_area = maxLeft - height[lMax]
            if curr_area > 0:
                total_area += curr_area
            lMax += 1
        else:
            if height[rMax] > maxRight:
                maxRight = height[rMax]
            curr_area = maxRight - height[rMax]
            if curr_area > 0:
                total_area += curr_area
            rMax -= 1

    return total_area


height = [4, 2, 0, 3, 2, 5]
print(trap(height))
