X = [1,2,4,5,13,26,8]

def sum_evens(nums):
    sum = 0
    for num in nums:
        if num % 2 != 0:
            sum = sum + num
    return sum

even_sum = sum_evens(X)
print(even_sum)