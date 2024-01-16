def findMaxLength(nums: list[int]) -> int:
    var = 0

    for x in list(nums):
        if x == 0:
            var -= 1
        else:
            var += 1

    return len(nums) - abs(var)


print(findMaxLength((1, 0, 1, 0, 1, 0, 1, 0)))
print(findMaxLength((1, 1, 1, 1, 1, 1)))
print(findMaxLength((0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1)))
print(findMaxLength((0, 1, 0)))
