# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytest_bdd import given,scenario,then,when,parsers

"""Login feature tests."""

# Constants

AUTOMATION_SITE = "http://automationpractice.com/index.php"

@pytest.mark.negative
@scenario('C://Users//wb14435//PycharmProjects//BDD_Python-master//tests//features//login_cart.feature','Invalid Customer login to the application')
def test_invalid_login():
    pass

@pytest.mark.positive
@scenario('C://Users//wb14435//PycharmProjects//BDD_Python-master//tests//features//login_cart.feature','Customer login to the application')
def test_login():
    pass

@pytest.mark.positive
@scenario('C://Users//wb14435//PycharmProjects//BDD_Python-master//tests//features//login_cart.feature','Add item to cart')
def test_add_cart():
    pass

@pytest.mark.positive
@scenario('C://Users//wb14435//PycharmProjects//BDD_Python-master//tests//features//login_cart.feature','Delete item from cart')
def test_delete_cart():
    pass

# Fixtures

@pytest.fixture(scope='session')
def browser():
    path = "C://Users//wb14435//PycharmProjects//BDD_Python-master//chromedriver.exe"
    b = webdriver.Chrome(executable_path=path)
    b.implicitly_wait(10)
    yield b

@given('I am in the website')
def i_am_in_the_website(browser):
    browser.get(AUTOMATION_SITE)    

@when('I press Sign in')
def i_press_sign_in(browser):
    browser.find_element_by_class_name("login").click()

@when(parsers.parse('I pass my e-mail: "{email}" and my password: "{password}"'))
def i_pass_my_email_and_my_password(browser,email,password):
    browser.find_element_by_id("email").send_keys(email)
    browser.find_element_by_id("passwd").send_keys(password)
    browser.find_element_by_id("SubmitLogin").click()

@then('I can see my account')
def i_can_see_my_account(browser):
    checkLogin = browser.find_element_by_class_name("account").text
    #Added this pause so it is possible to follow the test result
    assert "WB WB" in checkLogin

@given('I am in the homepage of website')
def i_am_in_the_website_homepage(browser):
    browser.find_element_by_id("header_logo").click()

@when('I navigate to any item')
def i_navigate_to_item(browser):
    browser.find_element_by_xpath("//img[@title='Printed Chiffon Dress']").click()

@when('I press Add to Cart button')
def i_press_add_to_cart(browser):
    browser.find_element_by_id("add_to_cart").click()

@then('I can see product added pop up')
def i_can_see_my_product_added_in_cart(browser):
    checkAdded = browser.find_element_by_xpath("//h2[contains(.,'Product successfully added to your shopping cart')]")
    assert checkAdded

@when('I navigate to cart page')
def i_navigate_to_cart_page(browser):
    browser.find_element_by_xpath("//a[@title='View my shopping cart']").click()

@when('I click on delete icon for added item')
def i_click_delete_icon_in_cart(browser):
    browser.find_element_by_id("7_34_0_582970").click()

@then('I can see empty cart message')
def i_can_see_my_product_added_in_cart(browser):
    checkMsg = browser.find_element_by_xpath("//p[contains(text(),'Your shopping cart is empty.')]")
    assert checkMsg

@then('I can see alert')
def i_can_see_alert_message(browser):
    checkAlert = browser.find_element_by_xpath("//div[@class='alert alert-danger']")
    assert checkAlert