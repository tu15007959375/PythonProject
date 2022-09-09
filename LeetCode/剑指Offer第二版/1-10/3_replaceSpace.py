def replaceSpace(s):
    return str.replace(s.encode('gbk'), ' ', '%20')


if __name__ == '__main__':
    print(replaceSpace("We are happy."))
