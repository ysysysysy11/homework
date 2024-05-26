
def add():
    result = 10 + 222
    print(f"10 + 222的结果是：{result}")

add()

def add(x, y):
    result = x + y
    print(f"{x} + {y}的结果是：{result}")

add(88,66)
print('hello world','回家吃饭',sep='<-->',end='-->')
print('酸菜饺子')
def fun_default_parameters(param1,param2=2):
    print(param1 + param2)

fun_default_parameters(1)
fun_default_parameters(1,5)
def fun_keyword_parameters(param1,param2=2):
    print(param1 - param2)

fun_keyword_parameters(param1=5,param2=2)

def fun_keyword_parameters(param1, param2=2):
    print(param1 - param2)


fun_keyword_parameters(5, param2=2)


def add(a,b):
    result = a + b
    return result

r = add(1, 2)
print(r)


def user_info(*args):
    print(args)

user_info('TOM')

user_info('TOM',18)

def user_info(**kwargs):
    print(kwargs)

user_info(name='TOM', age=18, id=110)



def sum(*nums):
    #定义一个变量，来保存结果
    result = 0
    #遍历元组，并将元组中的数进行累加
    for n in nums:
        result += n
    print(result)


sum(123,456,789,10,20,30,40)
def func_b():
    print("---2---")


def func_a():
    print("---1---")

    func_b()


    print("---3---")


#调用函数func_a
func_a()


def fun1(x,y):
    print("这是函数一")
    sum=x+y
    return sum


def fun2():
    print("这是函数二")
    sum=fun1(2, 3)
    print(sum)
fun2()

def max(x,y):
    return  x if x > y else y

def maxs(a,b,c,d):
    res1 = max(a,b)
    res2 = max(res1,c)
    res3 = max(res2,d)
    return res3

print(maxs(5,2,420,299))
def factorial(n):
    if n == 1:
        return 1
    else:
        return n *factorial(n-1)

num = 5
result = factorial(num)
print(f"The factorial of{num}is:{result}")
n = int(input())

def F(x):
    if x==1:
        return x
    else:
        return(F(x-1)+1)*2
print(F(n))

