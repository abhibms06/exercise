
# Palindromic substring


def palindromic_decomposition(s):
    arr = []

    for str_length in (range(1, len(s)+1)):
        index = 0
        tmp = ''
        end = str_length
        while index < len(s):
            str = s[index:end]

            if len(tmp) > 0:
                tmp = tmp + '|'

            if ispalindrome(str):
                tmp = tmp + str
                #index = index + str_length
                index = index + 1
                #end = end + str_length
                end = end + 1
            else:
                tmp = tmp + s[index]
                index = index + 1
                end = end + 1
            str_length = str_length

        arr.append(tmp)

    return set(arr)


def ispalindrome(s):
    str_length = len(s)
    start = 0
    end = str_length - 1

    while start < end:
        if s[start] != s[end]:
            return False

        start = start + 1
        end = end - 1

    return True



print('Enter a string')
s = input()

print(palindromic_decomposition(s))

#print(ispalindrome('ab'))