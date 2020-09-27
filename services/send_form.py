from selenium.webdriver.common.by import By


def send_form(form):
    button = form.find_element(By.CLASS_NAME, 'freebirdFormviewerViewNavigationSubmitButton')
    button.click()
