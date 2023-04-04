import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser


@allure.step("Check tests")
def test_check_button():
    browser = webdriver.Chrome()
    link = "http://the-internet.herokuapp.com/dynamic_controls"
    browser.get(link)
    check_button = (By.CSS_SELECTOR, 'input[type=checkbox]')
    check = WebDriverWait(browser, 10).until(EC.presence_of_element_located(check_button))
    check.click()


@allure.step("Remove butotn")
def test_remove_button():
    browser = webdriver.Chrome()
    link = "http://the-internet.herokuapp.com/dynamic_controls"
    browser.get(link)
    remove_button = (By.CSS_SELECTOR, '#checkbox-example > button')
    remove = WebDriverWait(browser, 10).until(EC.presence_of_element_located(remove_button))
    remove.click()
    

@allure.step("Input field")
def test_input_field():
    browser = webdriver.Chrome()
    link = "http://the-internet.herokuapp.com/dynamic_controls"
    browser.get(link)
    input_field = (By.CSS_SELECTOR, 'input[type=text]')
    input_f = WebDriverWait(browser, 10).until(EC.presence_of_element_located(input_field))
    assert not input_f.is_enabled()


@allure.step("Enable field")
def test_enable_button():
    browser = webdriver.Chrome()
    link = "http://the-internet.herokuapp.com/dynamic_controls"
    browser.get(link)
    enable_button = (By.CSS_SELECTOR, '#input-example > button')
    input_field = (By.CSS_SELECTOR, 'input[type=text]')
    input_f = WebDriverWait(browser, 10).until(EC.presence_of_element_located(input_field))
    enable = WebDriverWait(browser, 10).until(EC.presence_of_element_located(enable_button))
    enable.click()
    time.sleep(10)
    assert input_f.is_enabled()
