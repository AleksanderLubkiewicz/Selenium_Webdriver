#from selenium import webdriver
from selenium.webdriver.common.by import By




class Register:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome
        self.driver = driver
        # By.NAME
        self.input_first_name = "firstname"
        self.input_last_name = "lastname"
        self.input_mobile_number = "phone"
        self.input_email = "email"
        self.input_password = "password"
        self. input_confirm_password = "confirmpassword"
        # By.CSS
        self.button_sing_up = ".signupbtn"
        # By. XPATH
        self.alert = '//*[@id="headersignupform"]/div[2]/div'

    # Metoda wypełniająca formularz rejestracji nowego użytkownika.
    # Method filling out the new user registration form.
    def register(self, FirstName, LastName, Phone, Emial, Password):
        self.driver.find_element(By.NAME, self.input_first_name).send_keys(FirstName)
        self.driver.find_element(By.NAME, self.input_last_name).send_keys(LastName)
        self.driver.find_element(By.NAME, self.input_mobile_number).send_keys(Phone)
        self.driver.find_element(By.NAME, self.input_email).send_keys(Emial)
        self.driver.find_element(By.NAME, self.input_password).send_keys(Password)
        self.driver.find_element(By.NAME, self.input_confirm_password).send_keys(Password)
        self.driver.find_element(By.CSS_SELECTOR, self.button_sing_up).click()


    # Metoda pobierająca tekst alertów.
    # Method that retrieves alert text.
    def alert_text(self):
        text_alert = self.driver.find_element(By.XPATH, self.alert).text
        return text_alert

