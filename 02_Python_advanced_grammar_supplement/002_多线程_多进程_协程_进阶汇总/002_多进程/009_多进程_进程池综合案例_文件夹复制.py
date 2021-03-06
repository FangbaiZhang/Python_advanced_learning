# -*- coding:utf-8 -*-

# 复制一个文件夹，文件夹中有大量文件（成千上万的文件）
# 进程池实现多任务

import os, time
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
    print('开始copy文件:从%s-----到%s   文件名是：%s' % (old_folder_name, new_folder_name, file_name))
    # 打开读取原文件的内容，然后写入到新文件中
    # 以二进制方式打开，文件位于当前目录子文件夹中，文件路径使用/拼接
    old_file = open(old_folder_name + '/' + file_name, 'rb')
    content  = old_file.read()
    old_file.close()

    # 二进制方式将内容写入到新文件中，没有使用with打开，需要打开后记得关闭
    # 如果已经有文件，会直接打开，写入会覆盖以前的内容，没有就直接创建
    new_file = open(new_folder_name + '/' + file_name, 'wb')
    new_file.write(content)
    new_file.close()

    print('%s复制完成' % file_name)
    # 加入等待时间，便于观察，发现每次同时进行了三个任务
    # 等待时间结束后，开始下三个任务，取消睡眠时间，瞬间就完成了
    time.sleep(5)


def main():
    # 1. 获取用户要copy的文件夹的名字
    # （当前目录下，直接输入文件夹名称，
    # 不在当前路径下，将文件夹路径复制后输入，会自动打开路径下的文件夹）
    # 以当前目录下：009案例测试文件夹作为测试文件夹
    old_folder_name = input('请输入要要copy的文件夹的名字: ')
    print(old_folder_name)

    # 2. 创建一个新的文件夹，以旧文件夹名称为基准重命名后创建，如果存在就跳过
    # 当文件已存在，会出现错误[WinError 183] 当文件已存在时，无法创建该文件。: '009案例测试文件夹[复件]'
    try:
        new_folder_name = old_folder_name + '[复件]'
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹中所有待copy的文件名字,listdir返回文件夹中所有文件名称的列表
    file_names = os.listdir(old_folder_name)
    print(file_names)
    # 运行代码后发现，打印出所有文件名称后，有一个停顿，就是在执行第5步的for循环,创建多进程
    # for循环会将所有内容都存储在内存中，所以很占资源，使用yield生成器就可以解决该问题

    # 4. 创建进程池
    po = multiprocessing.Pool(3)

    # 5. 向进程池中添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name, ))

    # 关闭进程池和加入等待
    po.close()
    po.join()


if __name__ == '__main__':
    main()