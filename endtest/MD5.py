from random import Random
import hashlib


# 获取由4位随机大小写字母、数字组成的salt值
def create_salt(length=4):
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    random = Random()
    for i in range(length):
        # 每次从chars中随机取一位
        salt += chars[random.randint(0, len_chars)]
    return salt


# 加密原始密码+salt
def create_md5(pwd, salt):
    md5_obj = hashlib.md5()
    md5_obj.update((pwd + salt).encode("utf-8"))
    return md5_obj.hexdigest()


