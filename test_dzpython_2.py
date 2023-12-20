from new_test import num

def prettify_func_name(func, *argument):
    return f'{func.__name__.replace("_", " ").title()} [{", ".join([*argument])}]'
    # temp1 = func.__name__
    # temp2 = temp1.replace('_', ' ')
    # temp3 = temp2.title()
    # args = ", ".join([*argument])
    # temp4 = temp3 + ' [' + argument + ']'
    # temp4 = f'{temp3} [{args}]'
    # return temp4


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login",
                                           button_text="Register")


def open_browser(browser_name):
    actual_result = prettify_func_name(open_browser, browser_name)
    print(actual_result)
    print("Open Browser [Chrome]")
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = prettify_func_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = prettify_func_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == ("Find Registration Button On Login Page [https://companyname.com/login,"
                             " Register]")


def sum_result(a, b):
    result1 = a
    result2 = b
    assert (result2 + result1)
    print()

# функция, которая принмает в себя число и возвращает true если оно чётное и false если не чётное

def is_odd(num):
    # если число чётное то возращает true
    if num % 2 == 0:
        print("true")
    # и false если не чётное
    if num % 2 != 0:
        print("false")

#  проверить типы левой и правой части assert
num = 3
step1 = num % 2
step2 = 0
print (type(step1))
print (type(step2))



