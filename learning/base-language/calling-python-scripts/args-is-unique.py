#!/usr/bin/env python3

################################################################
# When ran, it will return 1 if all values passed in are unique and 0 if any repeat
# Maybe a good example of testing that each argument passed is unique?

# example: one repeates
# 5, 6, 6, 7
# 0

# Example all unique
# 6
# 1

# example: repeats
# 5,5
# 0

# example: unique
# 6,7
# 1

################################################################

def is_unique(s):
    s = list(s)
    s.sort()

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 0
    else:
        return 1

if __name__ == "__main__":
    print(is_unique(input()))