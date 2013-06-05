#!/usr/bin/python

# Anagram detection problem
# Take two strings of equal length and return if they are anagrams
# For eg: "heart" and "earth" are anagrams

# O(n^2) solution
def check_all_chars(str1, str2):
  str2_list = list(str2)

  for pos in range(len(str1)):
    found = False
    for letter in str2_list:
      if str1[pos] == letter:
        found = True
        break
    if not found:
      return False
  return True

# O(n^2) solution
def sort_and_compare(str1, str2):
  str1_list = sorted(list(str1))
  str2_list = sorted(list(str2))

  return str1_list == str2_list

# O(n) solution
def keep_char_count():
  pass


def main():
  s1 = "heart"
  s2 = "earth"
  print check_all_chars(s1, s2)
  print sort_and_compare(s1, s2)
  #keep_char_count(str1,str2)

if __name__ == "__main__":
  main()
