def longest_palindrome(s):
    if not s:
        return 0
    max_len = 1
    n = len(s)
    for sub_len in range(n, 0, -1):
        for i in range(n - sub_len + 1):
            sub = s[i:i+sub_len]
            if sub == sub[::-1]:
                max_len = max(max_len, sub_len)
                break
        if max_len >= sub_len:
            break
    return max_len

s = input() 
print(longest_palindrome(s))