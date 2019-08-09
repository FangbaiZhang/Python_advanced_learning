# 一个装饰器函数执行顺序

def deco(func):
    print("装饰器开始对原始函数进行装饰(我是外函数)：")
    def wrapper():
        print("...开始验证权限(我是内函数)...")
        func()
    return wrapper

@deco
def func_a():
    print("...权限验证通过...")

func_a()

# 单个装饰器函数执行顺序：
# 1. 主代码执行的时候，执行到@deco就对func_a开始装饰了,func_a在定义时候就被装饰了
# 开始执行deco函数，因此打印出：装饰器开始对原始函数进行装饰：
# 2. 相当于执行以下代码 func_a = deco(func_a)
# 3. 经过内函数装饰之后，返回内函数，此时原始函数func_a的地址实际已经指向了deco.wrapper函数的地址
# 4. 相当于已经有了一个新的func_a函数，主代码执行到func_a()这句代码时，实际上是执行deco.wrapper函数
# 5. 从而，首先打印出：...开始验证权限...
# 6. 接着执行wrapper中的func()，此时调用的才是原始函数func_a，打印出：...权限验证通过...

# 我们可以将最后的func_a()注释掉
# 代码执行到@deco时，外函数就会开始运行
# 真正执行func_a(),此时才开始执行内函数