from selenium import webdriver
from services.choice_and_save_answer import choice_and_save_answer
from services.open_three_tabs import open_three_tabs


URL = 'https://docs.google.com/forms/d/1MEHQTOFZ82ZVQ6BTGCbqXM3ja7TK4UyLEPFQdSS3pGo/viewform?edit_requested=true'
driver = webdriver.Firefox()
open_three_tabs(URL, driver)
choice_and_save_answer(driver)
