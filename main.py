from wxpy import *
import requests
import json


def do_it(nick):

    running = False
    bot = Bot(cache_path=True)
    # 好友统计信息
    # print(bot.friends().stats())
    # my_friend = bot.mps().search(nick)[0]
    # my_friend = bot.friends().search(nick)[0]
    my_friend = bot.groups().search(nick)[0]

    my_friend.send("智能机器人待机中...\n输入（芝麻开门）启动聊天功能")

    # 打印来自其他好友、群聊和公众号的消息
    # 全局注册必须现在前面, 否则后面的注册会被覆盖
    @bot.register(my_friend)
    def print_others(msg):
        global running
        if msg.type == 'Text':
            print('received msg: ', msg)
            if "芝麻开门" in msg.text:
                running = True
                return "聊天功能已启动，如果需要停止聊天，输入（芝麻关门）即可"
            elif "芝麻关门" in msg.text:
                running = False
                return "聊天功能已关闭，如果需要开启聊天，输入（芝麻开门）即可"
            elif running:
                reply_msg = tuling(msg.text)
                print('reply_msg:', reply_msg)
                return reply_msg


def tuling(content):
    """
    调用图灵机器人
    :param content: 聊天内容
    :return: 机器人回复内容
    """
    url = 'http://www.tuling123.com/openapi/api'
    param = {
        'key': 'aee98f38457842b2891d405f1fdaa701',
        'info': content,
        'userId': '237604'
    }
    r = requests.post(url, data=json.dumps(param))
    result = json.loads(r.content.decode())
    return result['text']


if __name__ == '__main__':
    # do_it()
    do_it('娃娃机特工队')

    # print(tuling('玩玩玩'))

    # 进入 Python 命令行、让程序保持运行
    embed()
