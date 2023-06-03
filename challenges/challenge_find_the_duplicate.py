def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    repeat_number = 0

    for number in nums:
        if type(number) is not int or number < 0:
            return False
        elif nums.count(number) > 1:
            repeat_number = number
    return repeat_number if repeat_number > 0 else False
