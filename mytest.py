
#if __name__=='__main__':
    #print("this is a module")
#    getvalue()

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 返回一个匿名函数
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 10:
        print(n)
    else:
        break

'''
sendlist = []
@asyncio.coroutine
def consumer():
    while True:
        print("I am consumer:hh")
        node = sendlist.pop()
        print("consumer:%s listlen:%d" % (node, len(sendlist)) )
        yield from asyncio.sleep(1)

@asyncio.coroutine
def producer():
    while True:
        msg = input()
        if msg :
            sendlist.append(msg)
            print("producer:%s listlen:%d" % (msg, len(sendlist)) )
            # tmp = sendlist.pop()
            # print("producer:%s listlen %d node:%s" % (msg, len(sendlist), tmp) )
        yield from asyncio.sleep(1)

loop = asyncio.get_event_loop()
tasks = [consumer(), producer()]
# loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
