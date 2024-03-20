class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        c_frequency = {}
        longest_length = 0
        for r, c in enumerate(s):
            if not c in c_frequency:
                c_frequency[c] = 0
            c_frequency[c] += 1

            cells_count = r - l + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_length = max(longest_length, cells_count)

            else:
                c_frequency[s[l]] -= 1
                if c_frequency[s[l]] == 0:
                    c_frequency.pop(s[l])
                l += 1

        return longest_length
