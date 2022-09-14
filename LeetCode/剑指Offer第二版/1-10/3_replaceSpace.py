# 替换空格
# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
def replaceSpace(s):
    return str.replace(s.encode('gbk'), ' ', '%20')


if __name__ == '__main__':
    print(replaceSpace("We are happy."))
