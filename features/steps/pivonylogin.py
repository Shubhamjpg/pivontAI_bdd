from behave import *
from selenium import webdriver

import time



@given('I launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('I open pivony homepage')
def openHomePage(context):
    context.driver.get("https://pivony.com/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    time.sleep(30)
    context.driver.find_element_by_xpath("//a[@id='hs-eu-confirmation-button']").click()
    context.driver.find_element_by_xpath("//span[contains(text(),'LOGIN')]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]").send_keys(user)
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/input[2]").send_keys(pwd)
    time.sleep(20)
    context.driver.find_element_by_id("//*[@id='recaptcha-anchor']/span").click()
    time.sleep(20)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/button[1]").click()


@then('user must successfully login to the Dashborad page')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/h1[1]").text
    assert text == "The right plan for your company's growth"
    context.driver.close()

