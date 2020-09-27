def open_three_tabs(URL, driver):
    driver.get(URL)

    for i in range(2):
        driver.execute_script('window.open()')
        driver.switch_to.window(driver.window_handles[i + 1])
        driver.get(URL)
