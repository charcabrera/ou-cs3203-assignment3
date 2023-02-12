def sum_list(nums=list[int, ...]):
    sum = 0
    for x in nums:
        sum = sum + x

    return sum


def product_list(nums=list[int, ...]):
    product = nums.pop()
    for x in nums:
        product = product * x

    return product
