def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    num_set = set()

    for number in nums:
        if type(number) != int or number <= 0:
            return False
        if number in num_set:
            return number
        else:
            num_set.add(number)
    return False
