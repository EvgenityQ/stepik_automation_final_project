import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    def __int__(self, *args, **kwargs):
        super(MainPage,self).__init__(*args, **kwargs)



