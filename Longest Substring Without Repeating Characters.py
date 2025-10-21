def length_of_longest_substring(text):
  seen = set()
  left = 0
  max_lenght = 0
  for right in range(len(text)):
    while text[right] in seen:
      seen.remove(text[left])
      left =+ 1
    seen.add(text[right])
    max_length = max(max_length, right - left + 1)
  return max_length

print(length_of_longest_substring("abccab"))  # Output: 3
print(length_of_longest_substring("pwwkew"))  # Output: 3
print(length_of_longest_substring("bbbbb"))   # Output: 1
print(length_of_longest_substring("abcabcbb"))# Output: 3
