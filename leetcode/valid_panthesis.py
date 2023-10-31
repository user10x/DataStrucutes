class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        valid_param_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        open_paranthesis_stack = []
        for char in s:
            if char in valid_param_map:
                if len(open_paranthesis_stack) == 0:
                    return False
                elif open_paranthesis_stack.pop() != valid_param_map[char]:
                    return False
            else:
                open_paranthesis_stack.append(char)

        if len(open_paranthesis_stack) > 0:
            return False
        return True

