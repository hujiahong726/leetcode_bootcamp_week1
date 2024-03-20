class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        count = 0
        curr_max = 0
        curr_min = -1
        for i, j in sorted(clips):
            if curr_max >= time or i > curr_max:
                    break
            if i > curr_min:
                curr_min = curr_max
                count += 1
            curr_max = max(j, curr_max)

        if curr_max >= time:
            return count
        else:
            return -1
