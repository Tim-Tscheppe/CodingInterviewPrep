# Given two strings, write a method to decide if one is a permutation of the other

# Going to use the sort() method
# Is this O(nlogn) or O(n)??
def CheckPermutation(s1, s2):
    return sorted(s1) == sorted(s2)

if __name__ == '__main__':
    print(CheckPermutation('cat','tac'))
    print(CheckPermutation('aaa','bbb'))