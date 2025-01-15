from collections import Counter
from collections import defaultdict

def anagrams_with_deafult_dict(word: str, test_word: str) -> bool:
  letter_count = defaultdict(int)
  for letter in word: 
    letter_count[word] += 1

  for char in test_word:
     if char not in letter_count: #If char not in word 
        return False
     letter_count[char] -= 1 
     if letter_count[char] < 0:
        return False

  return list(letter_count.values()) == [0 for i in range(len(letter_count))]
  
def anagram_with_counter(word: str, test_word: str) -> bool: 
  return Counter(word) == Counter(test_word)

def anagram_with_dict(word: str, test_word: str) -> bool:
  letter_count = dict()
  for letter in word: 
    if letter in letter_count:
      letter_count[letter] += 1
    else:
      letter_count[letter] = 1


  for char in test_word:
     if char not in letter_count:
        return False
     letter_count[char] -= 1 
     if letter_count[char] < 0:
        return False

  return list(letter_count.values()) == [0 for i in range(len(letter_count))]
  
# Test cases for anagrams_with_counter and anagrams_with_dict

# Test 1: Basic valid anagrams
assert anagram_with_counter("listen", "silent") == True, "Test 1 Failed (Counter)"
assert anagram_with_dict("listen", "silent") == True, "Test 1 Failed (Dict)"

# Test 2: Not anagrams (different letters)
assert anagram_with_counter("hello", "world") == False, "Test 2 Failed (Counter)"
assert anagram_with_dict("hello", "world") == False, "Test 2 Failed (Dict)"

# Test 3: Case sensitivity (should fail if case-sensitive)
assert anagram_with_counter("Listen", "Silent") == False, "Test 3 Failed (Counter)"
assert anagram_with_dict("Listen", "Silent") == False, "Test 3 Failed (Dict)"

# Test 4: Same word (self-anagram)
assert anagram_with_counter("word", "word") == True, "Test 4 Failed (Counter)"
assert anagram_with_dict("word", "word") == True, "Test 4 Failed (Dict)"

# Test 5: Different lengths
assert anagram_with_counter("abcd", "abc") == False, "Test 5 Failed (Counter)"
assert anagram_with_dict("abcd", "abc") == False, "Test 5 Failed (Dict)"

# Test 6: Words with spaces (should fail if spaces are not handled)
assert anagram_with_counter("a gentleman", "elegant man") == True, "Test 6 Failed (Counter)"
assert anagram_with_dict("a gentleman", "elegant man") == True, "Test 6 Failed (Dict)"

# Test 7: Empty strings
assert anagram_with_counter("", "") == True, "Test 7 Failed (Counter)"
assert anagram_with_dict("", "") == True, "Test 7 Failed (Dict)"

# Test 8: Anagrams with repeated letters
assert anagram_with_counter("aabbcc", "ccbbaa") == True, "Test 8 Failed (Counter)"
assert anagram_with_dict("aabbcc", "ccbbaa") == True, "Test 8 Failed (Dict)"

# Test 9: Non-alphabetic characters (should fail if not handled)
assert anagram_with_counter("123", "231") == True, "Test 9 Failed (Counter)"
assert anagram_with_dict("123", "231") == True, "Test 9 Failed (Dict)"

# Test 10: Non-anagrams with special characters
assert anagram_with_counter("abc!", "cab?") == False, "Test 10 Failed (Counter)"
assert anagram_with_dict("abc!", "cab?") == False, "Test 10 Failed (Dict)"

print("All tests passed!")