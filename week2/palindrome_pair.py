def is_palindrome(check):
        return check == check[::-1]

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        my_dict = {word:i for i, word in enumerate(words)}
        result = []
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in my_dict:
                        result.append([my_dict[back], i])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back in my_dict:
                        result.append([i, my_dict[back]])
        return result
