import sys

def printvalue():
    #print(_value)
    return ""
def getvalue():
    return 20
def setvalue(num):
    tmp = 20
    _value = num
    return tmp

if __name__=='__main__':
    #print("this is a module")
    getvalue()

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