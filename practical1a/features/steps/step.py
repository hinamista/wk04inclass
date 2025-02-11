from behave import *
from selenium import webdriver
from time import sleep

@given(u'Edge browser is Launched')
def launchEdgeBrowser(context):
    context.driver = webdriver.Edge()
    
@when(u'Open Formy page')
def openFormyPage(context):
    context.driver.get("https://formy-project.herokuapp.com/form")

@then(u'Verify Formy Title is present')
def verifyPagetitle(context):
    title = context.driver.title
    assert title == "Formy"

@then(u'Close Browser')
def closeBrowser(context):
    context.driver.close()

@then(u'Input Firstname "{firstName}" and Lastname "{lastName}"')
def inputName(context, firstName, lastName):
    context.driver.find_element("id", "first-name").send_keys(firstName)
    context.driver.find_element("id", "last-name").send_keys(lastName)

@then(u'Input multiple "{firstName}" and "{lastName}"')
def inputMultipleName(context, firstName, lastName):
    context.driver.find_element("id", "first-name").send_keys(firstName)
    context.driver.find_element("id", "last-name").send_keys(lastName)