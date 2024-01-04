from new_test import num
from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)

    if 6 < current_time.hour < 22:
        is_dark_theme = False
    else:
        is_dark_theme = True
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=22)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user is None and (current_time.hour >= 22 or current_time.hour <= 6):
        is_dark_theme = True
    elif dark_theme_enabled_by_user is None and (6 < current_time.hour < 22):
        is_dark_theme = False
    else:
        is_dark_theme = dark_theme_enabled_by_user

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Ivan", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Igor", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Irina", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None

    for i in users:
        if i['name'] == 'Olga':
            suitable_users = i

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет

    suitable_users = []

    for i in users:
        if i['age'] < 20:
            suitable_users.append(i)

    assert suitable_users == [
        {"name": "Igor", "age": 15},
        {"name": "Irina", "age": 18},
    ]


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







