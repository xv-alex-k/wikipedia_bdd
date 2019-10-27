from behave import *

from features.pages.login_page import LoginPage
from features.pages.main_page import MainPage


@given('I open url: "{url}"')
def step_impl(context, url):
    context.driver.get("{}{}".format(context.config.get("settings", "base_url"), url))


@given('I open home page')
def step_impl(context):
    context.driver.get(context.config.get("settings", "base_url"))


@when('I type "{username}" in username field')
def step_impl(context, username):
    login_page = LoginPage(context.driver)
    login_page.enter_username(username)


@when('I type "{password}" in password field')
def step_impl(context, password):
    login_page = LoginPage(context.driver)
    login_page.enter_password(password)


@when("I click login button")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login_button()


@when("I log in")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_username(context.config.get("user", "username"))
    login_page.enter_password(context.config.get("user", "password"))
    login_page.click_login_button()
    MainPage(context.driver)  # Verify user is on main page


@then("I see validation message for")
def step_impl(context):
    for row in context.table:
        context.execute_steps('''
        When I type "{username}" in username field
        When I type "{password}" in password field
        When I click element with text "Log in"
        Then I see element with text "{text}"
        '''.format(username=row["username"], password=row["password"], text=row["text"]))
