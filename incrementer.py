def incrementer(nums):
    output = []
    for i in range(len(nums)):
        if nums[i]+i+1 > 9:
            output.append(int(str(nums[i]+i+1)[-1]))
        else:
            output.append(nums[i]+i+1)
    return output
print(incrementer([]))
print(incrementer([1, 2, 3]))
print(incrementer([4, 6, 7, 1, 3]))
print(incrementer([3, 6, 9, 8, 9]))
print(incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]))
