import random

from selenium.webdriver.common.by import By


def save_choice_to_arr_and_click(question, choices_arr):
    for e in question:
        choices = e.find_elements(By.CLASS_NAME, 'freebirdFormviewerComponentsQuestionRadioChoice')

        choice = random.choice(choices)
        choice.click()

        choice_text = choice.find_element(By.TAG_NAME, 'span').text
        choices_arr.append(choice_text)