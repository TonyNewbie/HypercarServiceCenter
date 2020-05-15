def last_indexof_max(nums):
    index = 0
    for i in range(1, len(nums)):
        if nums[i] >= nums[index]:
            index = i
    return index
