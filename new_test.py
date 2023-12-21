
# функция, которая принмает в себя число и возвращает true если оно чётное и false если не чётное
def is_odd(num):

    # если число чётное то возращает true
    if num % 2 == 0:
        return True
    # и false если не чётное
    if num % 2 != 0:
        return False
# назначено значение 3 для переменной num
num = 3
x = is_odd(num)
y = False
print(x)
print(y)

assert x == y

