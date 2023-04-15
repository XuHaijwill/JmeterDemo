import hashlib
import random
import time
import sys

def test(UserID):
    ts = str(time.time())[:-8]
    NonceStr = str(ts) + str(random.randint(1,10000))
    data = "UserID=" + UserID+ "&" + "NonceStr=" + NonceStr + "固定的字符串"
    Sign = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    res = {'Sign:':Sign,'NonceStr':NonceStr}
    print(res)
    return res

test(UserID=sys.argv[1])

# if __name__ == '__main__':
#     print('PyCharm')
#     test('112')