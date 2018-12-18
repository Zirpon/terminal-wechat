# terminal-wechat

> this is a terminal wechat, supported send and receive wechat group or friend Text msg, in the python interactive mode
>
> based on [itchat](https://github.com/littlecodersh/ItChat)

- Friend name approximate matching search, List all Friend (增加了好友备注模糊搜索 好友昵称模糊搜索 好友全排列功能)
- Auto Reply to friend chat, auto reply random principle (增加了设置特定好友自动回复功能 设置回复消息 设置回复随机机制)
- Auto Group Chat reply (增加了设置特定群聊自动定时回复功能 设置回复消息 设置回复间隔 回复随机机制功能 支持图片 文字 语音 视频)
- Send msg Interface (发送消息接口)
- Auto download the vedio, voice, picture even it was retracted (记录视频语音图片消息包括撤回消息)
- record all the text msg even it was retracted (记录文本消息包括撤回消息)

usage:

```shell
> python
>>> import terchat
>>> terchat.start()
>>> terchat.send_msg("蛋挞 我要回家了", "@92c3dc453017be5ef25908102a925cd1")
>>> terchat.end()
>>> quit()
```
