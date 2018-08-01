import asyncio
import itchat
from itchat.content import *
import zlog

__doc__ = 'wechat module'

#if __name__ == "__main__":
#    print(__doc__)

#__name__ = "wechat"
instance = itchat.new_instance()

@instance.msg_register(TEXT, isGroupChat=True)
def group_replay(msg):
    FromUser = instance.search_chatrooms(userName=msg['FromUserName'])
    ToUser = instance.search_chatrooms(userName=msg['ToUserName'])
    # print(msg)
    # print("::::::::::::::::::::::::::::")
    # print(FromUser)
    # print("::::::::::::::::::::::::::::")
    # print(ToUser)
    # print("::::::::::::::::::::::::::::")
    chatroom = ( ((not FromUser) or (FromUser['NickName'] == 'A.Zirpon')) and ToUser ) or FromUser
    chatroomName = chatroom['NickName']
    chatroomUserName = chatroom['UserName']
    senderName = msg['ActualNickName']
    senderUserName = msg['ActualUserName']
    if senderName == '' :
        senderName = instance.search_chatrooms(userName=senderUserName)['NickName'] or "Empty senderName"

    print("\n\n+++++++++++++++ Group %s(%s) Chat +++++++++++++++++++++++" % (chatroomName, chatroomUserName))
    # print(chatroomName)
    # print(chatroom)
    # print("::::::::::::::::::::::::::::")
    # print("::::::::::::::::::::::::::::")
    # print("GroupChat[%s]:member[%s] send [%s]" % (chatroomName, senderName, msg['Text']))
    chatRoomLog = zlog.getLogger("Group",chatroomName)
    if chatRoomLog :
        chatRoomLog.debug("member[%s](%s) send [%s]" % (senderName, senderUserName, msg['Text']))
    # print("\n\n")
    # send to group
    # msg.user.send(u'@%s\u2005 I receuved: %s' % (senderName, msg['Text']))
    # send to phone
    # instance.send_msg("GroupChat:Dear %s\u2005,I am a robot,got your msg %s,My master will reply you soon,thanks" % (senderName, msg['Text']))

@instance.msg_register(TEXT, isFriendChat=True)
def friend_replay(msg):
    friend = instance.search_friends(userName=msg['FromUserName'])
    nickname = friend['NickName']
    username = friend['UserName']
    print("\n\n+++++++++++++++ Friend %s(%s) Chat +++++++++++++++++++++++" % (nickname,username))
    # print(msg)
    # print("::::::::::::::::::::::::::::")
    # print("FriendChat:friend[%s] send [%s]" % (nickname, msg['Text']))

    friendLog = zlog.getLogger("Friend",nickname)
    if friendLog :
        friendLog.debug("(%s) send [%s]" % (username, msg['Text']))

    # print("\n\n")
    instance.send_msg("FriendChat:Dear %s\u2005,I am a robot,got your msg %s,My master will reply you soon,thanks" % (nickname, msg['Text']))
    # instance.send_msg("Dear %s\u2005,I am a robot,got your msg %s,My master will reply you soon" % (nickname, msg['Text']), toUserName=msg['FromUserName'])

def start():
    instance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl') # enableCmdQR=True,
    instance.run(False,False)
    '''
    def coRecv():
        newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl') # enableCmdQR=True,
        newInstance.run()
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(coRecv())
    loop.close()
    '''

def end():
    instance.logout()