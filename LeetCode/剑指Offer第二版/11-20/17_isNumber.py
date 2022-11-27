# 表示数值的字符串
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 数值（按顺序）可以分成以下几个部分：
# 若干空格
# 一个小数或者整数
# （可选）一个'e'或'E'，后面跟着一个整数
# 若干空格
# 小数（按顺序）可以分成以下几个部分：
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 整数（按顺序）可以分成以下几个部分：
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if 'e' in s and 'E' in s:
            return False
        if 'e' in s and s.count('e') == 1:
            li = s.split('e')
            return (self.isinteger(li[0]) or self.isdecimal(li[0])) and self.isinteger(li[1])
        elif 'E' in s and s.count('E') == 1:
            li = s.split('E')
            return (self.isinteger(li[0]) or self.isdecimal(li[0])) and self.isinteger(li[1])
        else:
            return self.isinteger(s) or self.isdecimal(s)

    def isinteger(self, s: str) -> bool:
        if self.issymbol(s, '+'):
            return s.replace('+', '').isdigit()
        if self.issymbol(s, '-'):
            return s.replace('-', '').isdigit()
        return s.isdigit()

    def isdecimal(self, s: str) -> bool:
        if s.count('.') != 1:
            return False
        if self.issymbol(s, '+'):
            return s.replace('+', '').replace('.', '').isdigit()
        if self.issymbol(s, '-'):
            return s.replace('-', '').replace('.', '').isdigit()
        return s.replace('.', '').isdigit()

    def issymbol(self, s: str, s2) -> bool:
        if s2 in s and s.count(s2) == 1 and s.find(s2) == 0:
            return True


if __name__ == '__main__':
    sl = Solution()
    print(sl.isNumber('2e0'))
