def find_minimum(nums):
    minimum = float("inf")
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum

nums = [5, 4, 3, 2, 1]
print(find_minimum(nums))
