def sum(nums):
    res = 0
    for num in nums:
        res += num
    
    return res

nums = [7, 4, 3, 100, 2343243, 343434, 1, 2, 32]
print(sum(nums))