from selenium.webdriver.common.by import By
from settings import valid_phone, invalid_phone, invalid_phone_format, valid_password, invalid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_auth_by_phone_success(driver):
    phone_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    phone_field.send_keys(valid_phone)
    password_field.send_keys(valid_password)
    submit_button.submit()
    user_lc_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='user-name user-info__name']"))
    )

    assert "b2c.passport.rt.ru/account_b2c/" in driver.current_url
    assert user_lc_name.is_displayed()

def test_auth_by_phone_invalid_phone(driver):
    phone_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    phone_field.send_keys(invalid_phone)
    password_field.send_keys(valid_password)
    submit_button.submit()

    invalid_credentials = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-error='Неверный логин или пароль']"))
    )
    assert invalid_credentials.is_displayed()
    forgot_password = driver.find_element(By.ID, "forgot_password")
    assert "rt-link--muted" not in forgot_password.get_attribute("class")

def test_auth_by_phone_invalid_password(driver):
    phone_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    phone_field.send_keys(valid_phone)
    password_field.send_keys(invalid_password)
    submit_button.submit()

    invalid_credentials = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-error='Неверный логин или пароль']"))
    )
    assert invalid_credentials.is_displayed()
    forgot_password = driver.find_element(By.ID, "forgot_password")
    assert "rt-link--muted" not in forgot_password.get_attribute("class")

def test_auth_by_phone_invalid_phone_and_password(driver):
    phone_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    phone_field.send_keys(invalid_phone)
    password_field.send_keys(invalid_password)
    submit_button.submit()

    invalid_credentials = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-error='Неверный логин или пароль']"))
    )
    assert invalid_credentials.is_displayed()
    forgot_password = driver.find_element(By.ID, "forgot_password")
    assert "rt-link--muted" not in forgot_password.get_attribute("class")

def test_auth_by_phone_invalid_phone_format(driver):
    phone_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    phone_field.send_keys(invalid_phone_format)
    password_field.send_keys(valid_password)
    submit_button.submit()
    user_lc_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='user-name user-info__name']"))
    )

    assert "b2c.passport.rt.ru/account_b2c/" in driver.current_url
    assert user_lc_name.is_displayed()

def test_auth_by_phone_empty_phone(driver):
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    password_field.send_keys(valid_password)
    submit_button.submit()
    empty_number_alert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text() = 'Введите номер телефона']"))
    )

    assert empty_number_alert.is_displayed()

# Т.к. в чате пишут, что требования нужно дописать, то можно интерпретировать отсутсвие аллерта обязательного поля
# при попытке оставить поле пустым как багу.
def test_auth_by_phone_empty_password(driver):
    phone_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    submit_button = driver.find_element(By.NAME, "login")

    phone_field.send_keys(valid_phone)
    submit_button.submit()
    empty_password_alert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text() = 'Введите пароль']"))
    )

    assert empty_password_alert.is_displayed()


