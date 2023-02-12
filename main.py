#!/usr/bin/python3

from sys import stdin

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

def main():
    numbers = []
    for line in stdin:
        line = line.rstrip()
        numbers.append(int(line))

    # this is my first time using fstrings 🤨🤨🤨🤨
    print(f"Sum = {sum_list(numbers)}\nProduct = {product_list(numbers)}")


if __name__ == '__main__':
    main()
