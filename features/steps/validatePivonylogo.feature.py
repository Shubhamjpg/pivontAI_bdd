from time import sleep

from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('open pivony homepage')
def openHomePage(context):
    context.driver.get("https://pivony.com/")

@then('verify that the logo present on page')
def verifyLogo(context):
    sleep(30)
    context.driver.find_element_by_xpath("//a[@id='hs-eu-confirmation-button']").click()
    status = context.driver.find_element_by_xpath("//header/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
