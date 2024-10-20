# from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        #self.driver = webdriver.Chrome
        self.driver = driver
        # By NAME
        self.input_email = "username"
        self.input_password = "password"
        self.input_email_fp = "email"
        self.checkbox_remember = "remember"
        # By XPATH
        self.button_login = '//*[@id="loginfrm"]/button'
        self.button_sing_up = '//*[@id="loginfrm"]/div[2]/div[1]/a'
        self.button_forget_password = '//*[@id="loginfrm"]/div[2]/div[3]/a'
        self.button_reset_fp = '//*[@id="passresetfrm"]/div[2]/span/button'
        self.button_X_fp = '//*[@id="ForgetPassword"]/div/div/div[1]/button'

    # Metoda do logowania się.
    # Login method.
    def login(self, Email, Password):
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.kurs-selenium.pl/demo/login")
        self.driver.find_element(By.NAME, self.input_email).send_keys(Email)
        self.driver.find_element(By.NAME, self.input_password).send_keys(Password)
        self.driver.find_element(By.XPATH, self.button_login).click()

    # Metoda resetująca hasło.
    # Password reset method.
    def forget_password(self, Email):
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.kurs-selenium.pl/demo/login")
        self.driver.find_element(By.XPATH, self.button_forget_password).click()
        self.driver.find_element(By.NAME, self.input_email_fp).send_keys(Email)
        self.driver.find_element(By.XPATH, self.button_reset_fp).click()

    # Metoda do naciśnięcie przycisku SING UP
    # Method to press the SING UP button
    def sing_up(self):
        self.driver.find_element(By.XPATH, self.button_sing_up).click()







