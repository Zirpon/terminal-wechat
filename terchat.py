#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import itchat
from itchat.content import *
import zlog

__doc__ = 'wechat module'

#if __name__ == "__main__":
#    print(__doc__)

#__name__ = "wechat"
instance = itchat.new_instance()

# todo: instance 的接口应该封装一个异常捕获的头 在函数执行前
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

    # print("\n\n+++++++++++++++ Group %s(%s) Chat +++++++++++++++++++++++" % (chatroomName, chatroomUserName))
    # print(chatroomName)
    # print(chatroom)
    # print("::::::::::::::::::::::::::::")
    # print("::::::::::::::::::::::::::::")
    # print("GroupChat[%s]:member[%s] send [%s]" % (chatroomName, senderName, msg['Text']))
    # todo: 这里其实应该拉个线程/协程 来写日志的
    chatRoomLog = zlog.getLogger("Group",chatroomName)
    if chatRoomLog :
        chatRoomLog.debug("(%s)member[%s](%s) send [%s]" % (chatroomUserName, senderName, senderUserName, msg['Text']))
    # print("\n\n")
    # send to group
    # msg.user.send(u'@%s\u2005 I receuved: %s' % (senderName, msg['Text']))
    # send to phone
    # instance.send_msg("GroupChat:Dear %s\u2005,I am a robot,got your msg %s,My master will reply you soon,thanks" % (senderName, msg['Text']))

@instance.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_files(msg):
    FromUser = instance.search_chatrooms(userName=msg['FromUserName'])
    ToUser = instance.search_chatrooms(userName=msg['ToUserName'])
    chatroom = ( ((not FromUser) or (FromUser['NickName'] == 'A.Zirpon')) and ToUser ) or FromUser
    chatroomName = chatroom['NickName']
    chatroomUserName = chatroom['UserName']
    senderName = msg['ActualNickName']
    senderUserName = msg['ActualUserName']
    if senderName == '' :
        senderName = instance.search_chatrooms(userName=senderUserName)['NickName'] or "Empty senderName"
    
    chatRoomLog = zlog.getLogger("Group",chatroomName)
    if chatRoomLog :
        chatRoomLog.debug("(%s)member[%s](%s) send ![file](%s)" % (chatroomUserName, senderName, senderUserName, '../resource/'+msg['FileName']))
    #msg.download(msg['FileName'])   #这个同样是下载文件的方式
    #msg['Text'](msg['FileName'])      #下载文件
    msg["Text"]('./resource/'+msg['FileName'])
    #将下载的文件发送给发送者
    #itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg["FileName"]), msg["FromUserName"])
    #itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', './resource/'+msg['FileName']))

@instance.msg_register(TEXT, isFriendChat=True)
def friend_replay(msg):
    friend = instance.search_friends(userName=msg['FromUserName'])
    nickname = friend['NickName']
    username = friend['UserName']
    # print("\n\n+++++++++++++++ Friend %s(%s) Chat +++++++++++++++++++++++" % (nickname,username))
    # print(msg)
    # print("::::::::::::::::::::::::::::")
    # print("FriendChat:friend[%s] send [%s]" % (nickname, msg['Text']))

    friendLog = zlog.getLogger("Friend",nickname)
    if friendLog :
        friendLog.debug("(%s) send [%s]" % (username, msg['Text']))

    # print("\n\n")
    # instance.send_msg("FriendChat:Dear %s\u2005,I am a robot,got your msg %s,My master will reply you soon,thanks" % (nickname, msg['Text']))
    # instance.send_msg("Dear %s\u2005,I am a robot,got your msg %s,My master will reply you soon" % (nickname, msg['Text']), toUserName=msg['FromUserName'])

def start():
    instance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl') # enableCmdQR=True,
    instance.run(False,False)
    '''
    def coRecv():
        newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl') # enableCmdQR=True,
        newInstance.run()
    # EventLoop:
    loop = asyncio.get_event_loop()
    # coroutine
    loop.run_until_complete(coRecv())
    loop.close()
    '''

def send_msg(content,username):
    return instance.send_msg("terchat:%s" % content,toUserName=username)

def end():
    instance.logout()