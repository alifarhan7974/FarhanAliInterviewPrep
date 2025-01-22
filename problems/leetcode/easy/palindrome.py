class Solution: 
    # Two Pointer Pattern 
    def isPalindrome_more_storage(self, s: str) -> bool:
        return s[::-1] == s
    
    def isPalindrome_no_spaces(self, s: str) -> bool:
        start, end = 0, len(s) -1
        while start < end: 
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1


        return True

    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghiklmnopqrstuvwxyz1234567890"
        start, end = 0, len(s) -1
        while start <= end: 
            if s[start].lower() == " " or s[start].lower() not in alphabet:
                start += 1
                continue
            if s[end].lower() == " " or s[end].lower() not in alphabet:
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
            
        return True

test = Solution()

assert test.isPalindrome("") == True, "Empty String"

assert test.isPalindrome("AB") == False, "two letter word"

assert test.isPalindrome("0P") == False, "wrong testcase"

assert test.isPalindrome("A") == True, "Single Char"

assert test.isPalindrome("level") == True, "simple palindrome"


assert test.isPalindrome("     level                                               ") == True, "with spaces"

assert test.isPalindrome("Was it a car or a cat I saw?") == True, "with spaces"
