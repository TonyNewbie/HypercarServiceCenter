def range_sum(nums, a, b):
    sum_ = 0
    for number in nums:
        if a <= number <= b:
            sum_ += number
    return sum_


input_numbers = [int(digit) for digit in input().split()]
left_limit, right_limit = [int(limit) for limit in input().split()]
print(range_sum(input_numbers, left_limit, right_limit))
