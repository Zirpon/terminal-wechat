# terminal-wechat

> this is a terminal wechat, supported send and receive wechat group or friend Text msg, in the python interactive mode
>
> based on [itchat](https://github.com/littlecodersh/ItChat)

- Friend name approximate matching search (增加了好友模糊搜索功能)
- Auto Reply to friend chat, auto reply random principle (增加了设置特定好友自动回复功能)
- Auto Group Chat reply (增加了设置特定群聊自动定时回复功能)
- Send msg Interface (发送消息接口)
- Auto download the vedio, voice, picture even though it was retracted (记录视频语音图片消息)
- record all the text msg even though it was retracted (记录文本消息)

usage:

```shell
> python
>>> import terchat
>>> terchat.start()
>>> terchat.send_msg("蛋挞 我要回家了", "@92c3dc453017be5ef25908102a925cd1")
>>> terchat.end()
>>> quit()
```
