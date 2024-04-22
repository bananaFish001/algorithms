def average_followers(nums):
    sum = 0
    res = 0
    for num in nums:
        sum += num
    res = sum / len(nums)
    return res

nums = [1, 2, 3, 4, 5, 6, 7]
print(average_followers(nums))