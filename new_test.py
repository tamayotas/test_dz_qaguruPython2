
# функция, которая принмает в себя число и возвращает true если оно чётное и false если не чётное
def is_odd(num):
    # если число чётное то возращает true
    if num % 2 == 0:
        print("true")
    # и false если не чётное
    if num % 2 != 0:
        print("false")

num = 3
is_odd(num)

assert is_odd(num) == "false"

