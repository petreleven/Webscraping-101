from bs4 import element
from selenium import webdriver
from time import sleep, time

browser=webdriver.Firefox()
browser.get('http://inventwithpython.com')

sleep(10)
try:
    element=browser.find_element_by_class_name("card-img-top cover-thumb")
    print('Found <%s> element with that class name!'%(element.tag_name))
except:
    print('No element with such a name')