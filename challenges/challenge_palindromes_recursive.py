def is_palindrome_recursive(word, low_index, high_index):
    low_i = low_index
    high_i = high_index
    if word == '' or word[low_i] != word[high_i]:
        return False
    elif low_index >= high_index:
        return True
    else:
        low_i += 1
        high_i -= 1
        return is_palindrome_recursive(word, low_i, high_i)
