def merge_sort(string):
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = string[:middle]
    right = string[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    char1 = char2 = 0

    while char1 < len(left) and char2 < len(right):
        if left[char1] <= right[char2]:
            result.append(left[char1])
            char1 += 1

        else:
            result.append(right[char2])
            char2 += 1

    while char1 < len(left):
        result.append(left[char1])
        char1 += 1

    while char2 < len(right):
        result.append(right[char2])
        char2 += 1

    return ''.join(result)


def is_anagram(first_string, second_string):
    string1 = first_string.lower()
    string2 = second_string.lower()

    string1_ord = merge_sort(string1)
    string2_ord = merge_sort(string2)

    if len(string1_ord) == 0 or len(string2_ord) == 0:
        return (string1_ord, string2_ord, False)

    anagram = string1_ord == string2_ord

    return (string1_ord, string2_ord, anagram)
