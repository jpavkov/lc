def findMaxLength(nums: list[int]) -> int:
    # x = x value on plot
    # y = y value on plot
    # ans = value of longest sub array
    # dicto = key: y, value = x

    ans = 0
    y = 0
    dicto = {0: -1}

    for x, b in enumerate(nums):
        y += (b * 2) - 1
        if y not in dicto:
            dicto[y] = x
        else:
            ans = max(ans, (x-dicto[y]))

    return ans


print(findMaxLength((0, 0, 1)))
print(findMaxLength((1, 0, 1, 0, 1, 0, 1, 0)))
print(findMaxLength((1, 1, 1, 1, 1, 1)))
print(findMaxLength((0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1)))
print(findMaxLength((0, 1, 0)))
print(findMaxLength((0, 1, 1, 0, 1, 1, 1, 0)))
print(findMaxLength((0, 0, 1)))
