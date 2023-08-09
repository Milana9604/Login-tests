from selenium.webdriver.common.by import By
from settings import valid_phone, valid_email, valid_login, valid_ls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def test_auth_by_mail_invalid_mail_format(driver):
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")
    login_field = driver.find_element(By.ID, "username")
    phone_tab = driver.find_element(By.ID, "t-btn-tab-phone")
    mail_tab = driver.find_element(By.ID, "t-btn-tab-mail")
    login_tab = driver.find_element(By.ID, "t-btn-tab-login")
    ls_tab = driver.find_element(By.ID, "t-btn-tab-ls")

    login_field.send_keys(valid_phone)
    assert "rt-tab--active" in phone_tab.get_attribute("class")
    assert "rt-tab--active" not in mail_tab.get_attribute("class")
    assert "rt-tab--active" not in login_tab.get_attribute("class")
    assert "rt-tab--active" not in ls_tab.get_attribute("class")

    for _ in range(22):
        login_field.send_keys(Keys.BACK_SPACE)
    login_field.send_keys(valid_email)
    password_field.click()
    assert "rt-tab--active" in mail_tab.get_attribute("class")
    assert "rt-tab--active" not in phone_tab.get_attribute("class")
    assert "rt-tab--active" not in login_tab.get_attribute("class")
    assert "rt-tab--active" not in ls_tab.get_attribute("class")

    for _ in range(22):
        login_field.send_keys(Keys.BACK_SPACE)
    login_field.send_keys(valid_login)
    password_field.click()
    assert "rt-tab--active" in login_tab.get_attribute("class")
    assert "rt-tab--active" not in phone_tab.get_attribute("class")
    assert "rt-tab--active" not in mail_tab.get_attribute("class")
    assert "rt-tab--active" not in ls_tab.get_attribute("class")

    for _ in range(22):
        login_field.send_keys(Keys.BACK_SPACE)
    login_field.send_keys(valid_ls)
    password_field.click()
    assert "rt-tab--active" in ls_tab.get_attribute("class")
    assert "rt-tab--active" not in phone_tab.get_attribute("class")
    assert "rt-tab--active" not in mail_tab.get_attribute("class")
    assert "rt-tab--active" not in login_tab.get_attribute("class")