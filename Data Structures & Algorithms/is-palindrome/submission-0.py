class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(filter(str.isalnum, s)).lower()
        print(clean)
        reverse = clean[::-1]
        print(reverse)
        for i, v in enumerate(clean):
            if reverse[i] != v:
                return False
        return True