# Given an array of strings (str), group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

from collections import defaultdict


def group_anagrams(words):
    anagram_words = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        anagram_words[key].append(word)

    return list(anagram_words.values())



words_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words_list)
print(result)