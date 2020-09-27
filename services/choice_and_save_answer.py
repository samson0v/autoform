from selenium.webdriver.common.by import By
from services.save_choice_to_arr_and_click import save_choice_to_arr_and_click
from services.save_to_file import save_to_file
from services.send_form import send_form


def choice_and_save_answer(driver):
    i = 3
    for window_handle in reversed(driver.window_handles):
        driver.switch_to.window(window_handle)

        choices_arr = []
        form = driver.find_element(By.TAG_NAME, "form")
        question = form.find_elements(By.CLASS_NAME, 'freebirdFormviewerViewNumberedItemContainer')
        save_choice_to_arr_and_click(question, choices_arr)
        save_to_file(choices_arr, i)
        send_form(form)
        driver.close()
        i -= 1
