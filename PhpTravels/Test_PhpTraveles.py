from selenium import webdriver
from Register import Register
from Profil import Profil
from Login import Login
import time
import pytest


class PhpTravels:

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.http_login = 'http://www.kurs-selenium.pl/demo/login'
        self.http_register = 'http://www.kurs-selenium.pl/demo/register'
        self.http_profil = 'http://www.kurs-selenium.pl/demo/account/'
        self.FirstName = 'Sherlock'
        self.LastName = 'Holmes'
        self.Phone = '+44 20 1234567'
        self.Email = str(round(time.time())) + '@crime.com'
        self.Password = 'Doile#1'
        self.Address = 'Baker Street 221B'
        self.City = 'London'
        self.Region = 'Greater London'
        self.Zip = 'NW1 6XE'
        self.Country = 'GB'

    # Test utworzenia nowego konta użytkownika.
    # Test creating a new user account.
    def test_1(self):
        self.driver.get(self.http_register)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The registration panel loading time exceeded 5 seconds"
        self.TR1 = Register(self.driver)
        self.TR1.register(self.FirstName, self.LastName, self.Phone, self.Email, self.Password)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The loading time of the user panel exceeded 5 seconds"
        email.append(self.Email)
        time.sleep(5)
        self.url = self.driver.current_url
        assert self.url == self.http_profil, 'Invalid http address after user registration'
        self.TP1 = Profil(self.driver)
        self.TP1.button_profil_click()
        self.TP1.dane_1()
        FirstName, LastName, Phone, Email = self.TP1.dane_1()
        assert FirstName == self.FirstName, "The value retrieved from the user's profile does not match the entered data."
        assert LastName == self.LastName, "The value retrieved from the user's profile does not match the entered data."
        assert Phone == self.Phone, "The value retrieved from the user's profile does not match the entered data."
        assert Email == self.Email, "The value retrieved from the user's profile does not match the entered data."

    # Test logowania i formularza adresowego.
    # Login and address form test.
    def test_2(self):
        self.driver.get(self.http_login)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The login panel loading time exceeded 5 seconds"
        self.TL2 = Login(self.driver)
        self.TL2.login(email[0], self.Password)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The loading time of the user panel exceeded 5 seconds"
        time.sleep(5)
        self.url = self.driver.current_url
        assert self.url == self.http_profil, 'Wrong http address after login'
        self.TP2 = Profil(self.driver)
        self.TP2.button_profil_click()
        self.TP2.your_address(self.Address, '', self.City, self.Region, self.Zip, self.Country)
        self.TP2.logout()
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The login panel loading time exceeded 5 seconds"
        time.sleep(5)
        self.url = self.driver.current_url
        assert self.url == self.http_login, 'Wrong http address after logout'
        self.TL2.login(email[0], self.Password)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The loading time of the user panel exceeded 5 seconds"
        self.TP2.button_profil_click()
        self.TP2.dane_2()
        Address, City, Region, Zip, Country = self.TP2.dane_2()
        print(Address, City, Region, Zip, Country)
        assert Address == self.Address, "The value retrieved from the user's profile does not match the entered data."
        assert City == self.City, "The value retrieved from the user's profile does not match the entered data."
        assert Region == self.Region, "The value retrieved from the user's profile does not match the entered data."
        assert Zip == self.Zip, "The value retrieved from the user's profile does not match the entered data."
        assert Country == self.Country, "The value retrieved from the user's profile does not match the entered data."

    # Test zmiany hasła.
    # Password change test.
    def test_3(self):
        self.driver.get(self.http_login)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The login panel loading time exceeded 5 seconds"
        self.TL3 = Login(self.driver)
        self.TL3.login(email[0], self.Password)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The loading time of the user panel exceeded 5 seconds"
        self.TP3 = Profil(self.driver)
        self.TP3.button_profil_click()
        self.TP3.new_password('Doile#2')
        self.TP3.logout()
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The login panel loading time exceeded 5 seconds"
        self.TL3.login(email[0], "Doile#2")
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The loading time of the user panel exceeded 5 seconds"
        time.sleep(5)
        self.url = self.driver.current_url
        assert self.url == self.http_profil, 'Wrong http address after login'

    # Test alertu po niewprowadzeniu obowiązkowej wartości podczas rejestracji.
    # Alert test when a mandatory value is not entered during registration.
    def test_4(self):
        self.driver.get(self.http_register)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The registration panel loading time exceeded 5 seconds"
        self.TR4 = Register(self.driver)
        self.TR4.register('', self.LastName, self.Phone, self.Email, self.Password)
        text_alert = self.TR4.alert_text()
        assert text_alert == "The First name field is required.", 'Brak alertu lub treść niezgodna z założeniami'

    # Test alertu po wprowadzenie błędnego adresu email podczas rejestracji.
    # Alert test after entering an incorrect email address during registration.
    def test_5(self):
        self.driver.get(self.http_register)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The registration panel loading time exceeded 5 seconds"
        self.TR5 = Register(self.driver)
        self.TR5.register(self.FirstName, self.LastName, self.Phone, 'test#gmail.com', self.Password)
        text_alert = self.TR5.alert_text()
        assert text_alert == 'The Email field must contain a valid email address.', 'No alert or content not as intended'


    # Test alertu po wprowadzenie wcześniej użytego adresu email podczas rejestracji.
    # Test the alert after entering the previously used email address during registration.
    def test_6(self):
        self.driver.get(self.http_register)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The registration panel loading time exceeded 5 seconds"
        self.TR6 = Register(self.driver)
        self.TR6.register(self.FirstName, self.LastName, self.Phone, email[0], self.Password)
        text_alert = self.TR6.alert_text()
        assert text_alert == 'Email Already Exists.', 'No alert or content not as intended'

    # Test alertu po wprowadzenie zbyt krótkiego hasła podczas rejestracji.
    # Test alert after entering too short a password during registration.
    def test_7(self):
        self.driver.get(self.http_register)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The registration panel loading time exceeded 5 seconds"
        self.TR7 = Register(self.driver)
        self.TR7.register(self.FirstName, self.LastName, self.Phone, self.Email, '123')
        text_alert = self.TR7.alert_text()
        assert text_alert == 'The Password field must be at least 6 characters in length.', 'No alert or content not as intended'


    # Test alertu po błędnym potwierdzeniu hasła podczas rejestracji.
    # Alert test after incorrect password confirmation during registration.
    def test_8(self):
        self.driver.get(self.http_register)
        timing = self.driver.execute_script("return window.performance.timing")
        load_time = timing['loadEventEnd'] - timing['navigationStart']
        assert load_time < 5000, "The registration panel loading time exceeded 5 seconds"
        self.TR8 = Register(self.driver)
        self.TR8.register_2(self.FirstName , self.LastName, self.Phone, self.Email, self.Password, 'Doile#2')
        text_alert = self.TR8.alert_text()
        assert text_alert == 'Password not matching with confirm password.', 'No alert or content not as intended'





# Zbiór wykorzystany do zapisu adresu email na potrzebę testów.
# The set used to save the email address for testing purposes.
email = []

# Funkcje wywołujące metody testowe.
# Functions that call test methods.

# Test 1

def test_1():
    T1 = PhpTravels()
    T1.test_1()

# Test 2

def test_2():
    T2 = PhpTravels()
    T2.test_2()

# Test 3

def test_3():
    T3 = PhpTravels()
    T3.test_3()

# Test 4

def test_4():
    T4 = PhpTravels()
    T4.test_4()

# Test 5

def test_5():
    T5 = PhpTravels()
    T5.test_5()

# Test 6

def test_6():
    T6 = PhpTravels()
    T6.test_6()

# Test 7

def test_7():
    T7 = PhpTravels()
    T7.test_7()

# Test 8

def test_8():
    T8 = PhpTravels()
    T8.test_8()



