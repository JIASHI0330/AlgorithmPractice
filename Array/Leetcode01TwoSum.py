nums = [1, 3, 7, 9, 2]
target = 11

'''
The most basic solution is to use a nested loop. But the time complexity will be O(n2).
To optimize the solution, we want to just use one loop to iterate through each item in the array.
And then use a hash map to store the scanned number.

'''


def findTwoSum(nums, target):
    nums_dict = dict()
    for index, value in enumerate(nums):
        numToFind = target - value
        print("Number to find")
        print(numToFind)
        if numToFind in nums_dict:
            return [nums_dict[numToFind], index]
        nums_dict[nums[index]] = index
        print(nums_dict)
    return []


print(findTwoSum(nums, target))
