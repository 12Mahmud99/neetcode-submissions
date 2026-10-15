#time complexity is O(n)
#space complexity is O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [c for c in s if c.isalnum()]
        print(a)
        for i in range(len(a)):
            if (a[i].lower() != a[len(a) - 1 - i].lower()):
                return False
        return True