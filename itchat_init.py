import itchat
from itchat.content import *
import zlog

@itchat.msg_register(TEXT, isGroupChat=True)
def group_replay(msg):
    FromName = itchat.search_chatrooms(userName=msg['FromUserName'])['NickName']
    ToName = itchat.search_chatrooms(userName=msg['ToUserName'])['NickName']
    chatroomName = FromName
    senderName = msg['ActualNickName']
    #chatroom = itchat.search_chatrooms(userName=msg['FromUserName'])
    if FromName == 'A.Zirpon' :
        chatroomName = ToName
        #chatroom = itchat.search_chatrooms(userName=msg['ToUserName'])
    if senderName == '' :
        senderName = itchat.search_chatrooms(userName=msg['ActualUserName'])['NickName']

    # print("\n\n+++++++++++++++ Group %s Chat +++++++++++++++++++++++" % (chatroomName))
    # print(chatroomName)
    # print(chatroom)
    # print("::::::::::::::::::::::::::::")
    # print(msg)
    # print("::::::::::::::::::::::::::::")
    # print("GroupChat[%s]:member[%s] send [%s]" % (chatroomName, senderName, msg['Text']))
    chatRoomLog = zlog.Logger(logname="./log/GroupChat.log", loglevel=1, logger=chatroomName).getlog()
    chatRoomLog.debug("member[%s] send [%s]" % (senderName, msg['Text']))
    # print("\n\n")
    # send to group
    # msg.user.send(u'@%s\u2005 I receuved: %s' % (senderName, msg['Text']))
    # send to phone
    # itchat.send_msg("GroupChat:Dear %s\u2005,I am a robot,got your msg %s,My master will reply you soon,thanks" % (senderName, msg['Text']))

@itchat.msg_register(TEXT, isFriendChat=True)
def friend_replay(msg):
    nickname = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    # print("\n\n+++++++++++++++ Friend Chat +++++++++++++++++++++++")
    # print(msg)
    # print("::::::::::::::::::::::::::::")
    # print("FriendChat:friend[%s] send [%s]" % (nickname, msg['Text']))

    friendLog = zlog.Logger(logname="./log/FriendChat.log", loglevel=1, logger=nickname).getlog()
    friendLog.debug("send [%s]" % (msg['Text']))

    # print("\n\n")
    itchat.send_msg("FriendChat:Dear %s\u2005,I am a robot,got your msg %s,My master will reply you soon,thanks" % (nickname, msg['Text']))
    # itchat.send_msg("Dear %s\u2005,I am a robot,got your msg %s,My master will reply you soon" % (nickname, msg['Text']), toUserName=msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run()