"""
test cases:
[7,1,2,3,9]   return 7*4=28
[]            return 0
[7]           return 0
[6,9,3,4,5,8] return between[6,8]=30 and [9,8]=32
"""

'''
Brute force methods
'''
# def maxArea(water_containers):
#     max_area = 0
#     for i in range(len(water_containers)):
#         a = water_containers[i]
#         for j in range(1, len(water_containers)):
#             b = water_containers[j]
#             height = min(a, b)
#             length = j - i
#             area = length * height
#             if area > max_area:
#                 max_area = area
#     return max_area

'''
Use two shifting pointers to do this question
Set the first number to be left pointer and the last number to be the right pointer
Then we calculate the area
'''

water_containers = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def maxArea(water_containers):
    max_area = 0
    leftPointer = 0
    rightPointer = len(water_containers) - 1
    while leftPointer < rightPointer:
        if water_containers[leftPointer] <= water_containers[rightPointer]:
            length = rightPointer - leftPointer
            current_area = water_containers[leftPointer] * length
            max_area = max(max_area, current_area)
            leftPointer += 1
        else:
            length = rightPointer - leftPointer
            current_area = water_containers[rightPointer] * length
            max_area = max(max_area, current_area)
            rightPointer -= 1

    return max_area


print(maxArea(water_containers))
