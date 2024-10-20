#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Profil:
    def __init__(self, driver):
        #self.driver = webdriver.Chrome
        self.driver = driver
        # Profil
        # By XPATCH
        self.button_profil = '//*[@id="body-section"]/div[2]/div[2]/div/div[1]/ul/li[2]/a'
        self.button_submit = '//*[@id="profilefrm"]/div/div[3]/div[3]/button'
        self.button_list = '/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a'
        self.button_logout = '/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[2]/a'
        # By NAME
        self.input_first_name = 'firstname'
        self.input_last_name = "lastname"
        self.input_mobile_number = "phone"
        self.input_email = "email"
        self.input_password = "password"
        self. input_confirm_password = "confirmpassword"
        self.input_address = "address1"
        self.input_address_2 = "address2"
        self.input_city = 'city'
        self.input_region = 'state'
        self.input_zip_code = 'zip'
        self.list_contry = 'country'

    # Metodauzupełniające dane adresowe w zakładce profil.
    # function additional address data in the profile.
    def your_address(self, address, address_2, city, region, zip, country):
        self.driver.find_element(By.NAME, self.input_address).clear()
        self.driver.find_element(By.NAME, self.input_address).send_keys(address)
        self.driver.find_element(By.NAME, self.input_address_2).clear()
        self.driver.find_element(By.NAME, self.input_address_2).send_keys(address_2)
        self.driver.find_element(By.NAME, self.input_city).clear()
        self.driver.find_element(By.NAME, self.input_city).send_keys(city)
        self.driver.find_element(By.NAME, self.input_region).clear()
        self.driver.find_element(By.NAME, self.input_region).send_keys(region)
        self.driver.find_element(By.NAME, self.input_zip_code).clear()
        self.driver.find_element(By.NAME, self.input_zip_code).send_keys(zip)
        Select(self.driver.find_element(By.NAME, self.list_contry)).select_by_value(country)
        self.driver.find_element(By.XPATH, self.button_submit).click()

    # Metoda do wylogowania się.
    # Function to log out.
    def logout(self):

        self.driver.get("http://www.kurs-selenium.pl/demo/account/logout/")


    # Metoda pobierająca dane z panelu użytkownika.
    # Method that retrieves data from the user panel.
    def dane_1(self):
        FirstName = self.driver.find_element(By.NAME, self.input_first_name).get_attribute('value')
        LastName = self.driver.find_element(By.NAME, self.input_last_name).get_attribute('value')
        Phone = self.driver.find_element(By.NAME, self.input_mobile_number).get_attribute('value')
        Email = self.driver.find_element(By.NAME, self.input_email).get_attribute('value')
        return FirstName, LastName, Phone, Email

    # Metoda naciskająca przycisk profil.
    # Method pressing the profile button.
    def button_profil_click(self):
        self.driver.find_element(By.XPATH, self.button_profil).click()

    # Metoda pobierająca dane adresowe
    # Method that retrieves address data.
    def dane_2(self):
        Address = self.driver.find_element(By.NAME, self.input_address).get_attribute('value')
        City = self.driver.find_element(By.NAME, self.input_city).get_attribute('value')
        Region = self.driver.find_element(By.NAME, self.input_region).get_attribute('value')
        Zip = self.driver.find_element(By.NAME, self.input_zip_code).get_attribute('value')
        Country = self.driver.find_element(By.NAME, self.list_contry).get_attribute('value')
        return Address, City, Region, Zip, Country

    # Metoda zmieniająca hasło
    # Password changing method.
    def new_password(self, password_2):
        self.driver.find_element(By.NAME, self.input_password).send_keys(password_2)
        self.driver.find_element(By.NAME, self.input_confirm_password).send_keys(password_2)
        self.driver.find_element(By.XPATH, self.button_submit).click()
