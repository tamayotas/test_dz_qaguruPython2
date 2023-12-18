from datetime import time

def prettify_func_name(func, *argument):
    return f' {func.__name__.replace("_", " ").title()} [{", ".join([*argument])}]'
    #temp1 = func.__name__
    #temp2 = temp1.replace('_', ' ')
    #temp3 = temp2.title()
    #args = ", ".join([*argument])
    #temp4 = temp3 + ' [' + argument + ']'
    #temp4 = f'{temp3} [{args}]'
    #return temp4

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login",
                                           button_text="Register")


def open_browser(browser_name):
    actual_result = prettyfy_func_name(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = prettyfy_func_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = prettyfy_func_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == ("Find Registration Button On Login Page [https://companyname.com/login,"
                             " Register]")







                                                                                                 ""
                                                                                                 "")

