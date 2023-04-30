# Implement and algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Going to use a hashset in order to get a first pass O(1) Solution
def IsUnique(s):
    Hashset = set()
    for n in s:
        if n in Hashset:
            return False
        else:
            Hashset.add(n)
    return True

if __name__ == '__main__':
    print(IsUnique('aaaaaaaa'))
    print(IsUnique('abcdefg'))


