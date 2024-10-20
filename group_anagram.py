from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lst = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
        anagrams = defaultdict(list)
        new_lst = []

        for word in lst:
           sorted_word = ''.join(sorted(word))
           anagrams[sorted_word].append(word)

        for i in anagrams:
            new_lst.append(list(anagrams[i]))
        return new_lst