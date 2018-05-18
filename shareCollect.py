from wxpy import *
import pymysql


def do_it(nick):

    bot = Bot(cache_path=True)
    # 好友统计信息
    my_friend = bot.friends().search(nick)[0]

    @bot.register(my_friend)
    def print_point(msg):

        print("text", msg.text)
        print("url", msg.url)


def collect(title, url):
    pass


if __name__ == '__main__':
    do_it('啥')

    # 进入 Python 命令行、让程序保持运行
    embed()
