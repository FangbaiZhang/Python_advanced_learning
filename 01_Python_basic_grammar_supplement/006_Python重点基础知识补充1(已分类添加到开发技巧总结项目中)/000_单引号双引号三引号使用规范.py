# 前后三个单引号或双引号代表包裹注释内容，推荐使用三个单引号
'''
注释内容
'''

# 双引号:纯粹的字符串，用于打印显示，字符串的拼接，使用双引号

# 单引号，除了纯粹的字符串，其它的字符串，参数等都用单引号，比如字典的键值，类传入的参数等等

# 当有重叠使用时，不能重复用双引号或者单引号

# 字符串内部有双引号，外面使用单引号
# 推荐下面第二种方法

print("我有一本书，书的名字是 'python' ")
print('我有一本书，书的名字是 "python" ')

# 下面案例单引号，双引号，三引号综合使用
def pet(animal_type, pet_name):
    '''
    传入两个参数
    显示宠物的信息
    '''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

pet('hamster', 'harry')

