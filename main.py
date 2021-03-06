from wxpy import *
import requests
import json


def do_it(nick):

    bot = Bot(cache_path=True)
    # 好友统计信息
    # print(bot.friends().stats())
    # my_friend = bot.mps().search(nick)[0]
    my_friend = bot.friends().search(nick)[0]
    # my_friend = bot.groups().search(nick)[0]

    # 打印来自其他好友、群聊和公众号的消息
    # 全局注册必须现在前面, 否则后面的注册会被覆盖
    @bot.register()
    def print_others(msg):
        if msg.is_at:
            print('received msg: ', msg)
            if msg.type == 'Text':
                reply_msg = tuling(msg.text)
            else:
                reply_msg = '抱歉, 我不明白你在说啥子'
            print('reply_msg:', reply_msg)
            return reply_msg

    @bot.register(my_friend)
    def print_point(msg):
        if msg.is_at:
            return "hello world"
        else:
            return '非服务对象'


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
    do_it('啥')

    # print(tuling('玩玩玩'))

    # 进入 Python 命令行、让程序保持运行
    embed()
