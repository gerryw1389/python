class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            curr_str = '1'
        for i in range(1, n):
            if i+1 == n:
                return self.say(curr_str)
            else:
                curr_str = self.say(curr_str)

    def say(self, s: str) -> str:
        if s == '1':
            return '11'
        idx = 0
        string = ''
        while idx != len(s):
            curr_int = s[idx]
            counter = 0
            while idx != len(s) and s[idx] == curr_int:
                counter += 1
                idx += 1
            string += str(counter) + curr_int
        return string