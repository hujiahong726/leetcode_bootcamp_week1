class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ''

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_num = 0
                curr_str = ""
            elif c == "]":
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += c

        return curr_str
