# -*- coding:utf-8 -*-

import threading
import time


def test1():
    for i in range(5):
        print('-----test1-----%d-----' % i)
        time.sleep(1)


def main():

    # 打印第一次，显示当前所有进程
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)

    # 打印第二次，显示当前所有进程
    print(threading.enumerate())

    # setDaemon(True)设置为守护线程
    t1.setDaemon(True)
    t1.start()

    # 打印第三次，显示当前所有进程
    print(threading.enumerate())

    # 打印第四次，显示当前所有进程
    time.sleep(3)
    print(threading.enumerate())

    print('主线程代码执行完毕')


if __name__ == '__main__':
    main()

# 调用Thread时候创建线程对象
# 子线程开始时间：对象调用start函数后线程开始执行
# 子线程结束时间：线程调用的函数执行结束
# 通过打印不同时间下的线程，可以发现主线程和子线程执行顺序

# 非守护线程：默认多线程是非守护
# main()函数执行完毕了，子线程还在继续执行

# 守护线程：setDaemon(True)
# 主代码结束执行结束后，子线程直接结束，即使还没有执行完成

# 为了使非守护线程，子线程执行结束后再执行主线程剩下的代码
# 可以使用join函数等待子线程执行结束 参考009