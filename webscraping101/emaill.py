from selenium import webdriver
from time import sleep

def login_email(email,msg):
    web='https://login.yahoo.com/?.intl=us'
    browser=webdriver.Firefox()
    browser.get(web)
    sleep(10)
    username=browser.find_element_by_id('login-username')
    username.send_keys('gigivitale')

    next=browser.find_element_by_class_name('button-container')
    next.click()
    sleep(5)
    url=browser.current_url
    browser.get(url)
    password=browser.find_element_by_id('login-passwd')
    password.send_keys('11207203001')
    
    next=browser.find_element_by_id('login-signin')
    next.click()

    url=browser.current_url
    browser.get(url)
    sleep(5)
    icon=browser.find_element_by_id('ybarMailLink')
    icon.click()
    sleep(5)
    url=browser.current_url
    browser.get(url)

    compose=browser.find_element_by_link_text('Compose')
    compose.click()
    sleep(5)
    url=browser.current_url
    browser.get(url)
    sleep(10)

    message=browser.find_element_by_id('message-to-field')
    message.send_keys(email)
    body=browser.find_element_by_id('editor-container')
    body.send_keys(msg)

    send=browser.find_element_by_link_text('Send')
    send.click()





def inputs_():
    email=input('Enter Email :')
    msg=input('Enter message :')
    login_email(email,msg)

inputs_()