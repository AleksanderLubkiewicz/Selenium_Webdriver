import sys
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


# Adres strony rejestracyjnej Legimi.
driver.get("https://www.legimi.pl/konto/zarejestruj/")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Zamknięcie zapytania o Cookis
try:
    driver.implicitly_wait(10)
    X_Cookis = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    if X_Cookis:
        X_Cookis.click()
except:
    print("Powiadomienie o pliku Cookis nie pojawiło się, lub nie zostało zamknięte")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Wyszukanie elementów na stronie
WE = 0
#Input - Nazwa użytkowanika
try:
    Nazwa_U = driver.find_element(By.NAME, "UserName")
except:
    print("Nie znaleziono okna tekstowego 'Nazwa użytkownika'. Brak możliwości przeprowadzenia testu.'")
    WE += 1

#Input - Adres e-mail
try:
    Email = driver.find_element(By.NAME, "Email")
except:
    print("Nie znaleziono okna tekstowego 'E-mail'. Brak możliwości przeprowadzenia testu.'")
    WE += 1

#Input - Hasło
try:
    Hasło = driver.find_element(By.NAME, "Password")
except:
    print("Nie znaleziono okna tekstowego 'Hasło'. Brak możliwości przeprowadzenia testu.'")
    WE += 1

#Input - Powtóż hasło
try:
    P_Hasło = driver.find_element(By.NAME, "ConfirmPassword")
except:
    print("Nie znaleziono okna tekstowego 'Powtórz hasło'. Brak możliwości przeprowadzenia testu.'")
    WE += 1

# Checkbox - Akceptacja regulaminu
try:
    Akceptacja = driver.find_element(By.CSS_SELECTOR, ".mdl-checkbox__ripple-container:nth-child(6)")
except:
    print("Nie znaleziono cheeckoxa 'Akceptacja regulaminu'. Brak możliwości przeprowadzenia testu.'")
    WE += 1


# Przycisk - Zarejestruj.
try:
    Zarejestruj = driver.find_element(By.CSS_SELECTOR, "*[data-test='register-button']")
except:
    print("Nie znaleziono przycisku 'Zarejestruj'. Brak możliwości przeprowadzenia testu.'")
    WE += 1
if WE != 0:
    input("Naciśnij ENTER, żeby zakończyć test")
    exit()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Test 1.
# Lista błędów dla Test 1.
T1_E = []

# Naciśnięcie przycisku "Zarejestruj"

try:
    Zarejestruj.click()
except Exception as e:
    T1_E1 = "Nie udało się nacisnąć przycisku 'Zarejestruj"
    T1_E.append(T1_E1)

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Nazwa użytkownika"
try:
    T1_E_NU = driver.find_element(By.ID, "UserName-error")
    if T1_E_NU:
        if T1_E_NU.text != "Pole wymagane":
            T1_E12 = "Tekst informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Pole wymagane'" "\n" \
                     "Wyświetlony tekst - " + T1_E_NU.text
            T1_E.append(T1_E12)
except:
    T1_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Nazwa użytkownika'"
    T1_E.append(T1_E2)

try:
    T1_C_NU = T1_E_NU.value_of_css_property(property_name= "Color")
    if T1_C_NU:
        if T1_C_NU != "rgb(213, 0, 0)":
            T1_E13 = "Kolor informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T1_C_NU
            T1_E.append(T1_E13)
except:
    T1_E3 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Nazwa użytkownika'"
    T1_E.append(T1_E3)

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Adres e-mail"
try:
    T1_E_E = driver.find_element(By.ID, "Email-error")
    if T1_E_E:
        if T1_E_E.text != "Pole wymagane":
            T1_E14 = "Tekst informacji o błędzie pod polem testowym 'E-mail' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Pole wymagane'" "\n" \
                     "Wyświetlony tekst - " + T1_E_E.text
            T1_E.append(T1_E14)
except:
    T1_E4 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'E-mail'"
    T1_E.append(T1_E4)

try:
    T1_C_E = T1_E_E.value_of_css_property(property_name= "Color")
    if T1_C_E:
        if T1_C_E != "rgb(213, 0, 0)":
            T1_E15 = "Kolor informacji o błędzie pod polem testowym 'E-mail' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T1_C_E
            T1_E.append(T1_E15)
except:
    T1_E5 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'E-mail'"
    T1_E.append(T1_E5)

# Pobranie informacji o błędzie pod polem tekstowym "Hasło"
try:
    T1_E_H = driver.find_element(By.ID, "Password-error")
    if T1_E_H:
        if T1_E_H.text != "Pole wymagane":
            T1_E16 = "Tekst informacji o błędzie pod polem testowym 'Hasło' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Pole wymagane'" "\n" \
                     "Wyświetlony tekst - " + T1_E_H.text
            T1_E.append(T1_E16)
except:
    T1_E6 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Hasło'"
    T1_E.append(T1_E6)

try:
    T1_C_H = T1_E_H.value_of_css_property(property_name= "Color")
    if T1_C_H:
        if T1_C_H != "rgb(213, 0, 0)":
            T1_E17 = "Kolor informacji o błędzie pod polem testowym 'Hasło' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T1_C_H
            T1_E.append(T1_E17)
except:
    T1_E7 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Hasło'"
    T1_E.append(T1_E7)


# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Powtórz hasło"
try:
    T1_E_PH = driver.find_element(By.ID, "ConfirmPassword-error")
    if T1_E_PH:
        if T1_E_PH.text != "Pole wymagane":
            T1_E18 = "Tekst informacji o błędzie pod polem testowym 'Powtórz hasło' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Pole wymagane'" "\n" \
                     "Wyświetlony tekst - " + T1_E_PH.text
            T1_E.append(T1_E18)
except:
    T1_E8 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Powtórz hasło'"
    T1_E.append(T1_E8)

try:
    T1_C_PH = T1_E_PH.value_of_css_property(property_name= "Color")
    if T1_C_PH:
        if T1_C_PH != "rgb(213, 0, 0)":
            T1_E19 = "Kolor informacji o błędzie pod polem testowym 'Powtórz hasło' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T1_C_PH
            T1_E.append(T1_E19)
except:
    T1_E9 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Powtórz hasło'"
    T1_E.append(T1_E9)


# Pobranie informacji o błędzie pod checkboxem  "Akceptacja regulaminu"

try:
    T1_E_AR = driver.find_element(By.ID, "AcceptDiscipline-error")
    if T1_E_AR:
        if T1_E_AR.text != "Zgoda obowiązkowa. Zaznacz to pole, jeśli chcesz kontynuować":
            T1_E20 = "Tekst informacji o błędzie pod checkboxem 'Akceptacja regulaminu' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Zgoda obowiązkowa. Zaznacz to pole, jeśli chcesz kontynuować'" "\n" \
                     "Wyświetlony tekst - " + T1_E_AR.text
            T1_E.append(T1_E20)
except:
    T1_E10 = "Nie znaleziono informacji o błędzie pod checkboxem 'Akceptacja regulaminu'"
    T1_E.append(T1_E10)

try:
    T1_C_AR = T1_E_AR.value_of_css_property(property_name= "Color")
    if T1_C_AR:
        if T1_C_AR != "rgb(213, 0, 0)":
            T1_E21 = "Kolor informacji o błędzie pod checkboxem 'Akceptacja regulaminu' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T1_C_AR
            T1_E.append(T1_E21)

except:
    T1_E11 = "Nie znaleziono informacji o kolorze tekstu pod checkboxem 'Akceptacja regulaminu'"
    T1_E.append(T1_E11)


# Raport z Test 1
T = 0
print("Raport  z testu informacji o błędach w formularzu rejestracyjnym na stronie internetowej Legimi")
D = date.today()
print("Wykonano - " + str(D))

print(".....................................................................................................")

if T1_E == []:
    print("Test 1 - Zaliczony")
    T += 1
else:
    print("Test 1 - Wykryto błędy / Niezaliczony")
    for e in T1_E:
        print(e)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 2
# Lista błędów testu 2.

T2_E = []

# Wprowadzenie tekstu do okna tekstowego 'Nazwa użytkownika' i przejście do kolejnego okna tekstowego.
Nazwa_U.click()
Nazwa_U.send_keys("NNNN")
Email.click()

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Nazwa użytkownika"
try:
    T2_E_NU = driver.find_element(By.ID, "UserName-error")
    if T2_E_NU:
        if T2_E_NU.text != "Nazwa użytkownika powinna zawierać minimum 5 znaków, składać się z liter " \
                           "(bez polskich ogonków), cyfr, myślników lub znaków podkreślenia i nie może "\
                           "zawierać samych cyfr":
            T2_E1 = "Tekst informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Nazwa użytkownika powinna zawierać minimum 5 znaków, składać się z liter ""\n" \
                    "(bez polskich ogonków), cyfr, myślników lub znaków podkreślenia i nie może zawierać samych cyfr'" "\n" \
                     "Wyświetlony tekst - " + T2_E_NU.text
            T2_E.append(T2_E1)
except:
    T2_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Nazwa użytkownika'"
    T2_E.append(T2_E2)

try:
    T2_C_NU = T2_E_NU.value_of_css_property(property_name= "Color")
    if T2_C_NU:
        if T2_C_NU != "rgb(213, 0, 0)":
            T2_E3 = "Kolor informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T2_C_NU
            T2_E.append(T2_E3)
except:
    T2_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Nazwa użytkownika'"
    T2_E.append(T2_E4)


# Raport z Test 2

print(".....................................................................................................")

if T2_E == []:
    print("Test 2 - Zaliczony")
    T += 1
else:
    print("Test 2 - Wykryto błędy / Niezaliczony")
    for e in T2_E:
        print(e)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 3
# Lista błędów testu 3.

T3_E = []

# Wprowadzenie tekstu do okna tekstowego 'Nazwa użytkownika' i przejście do kolejnego okna tekstowego.
Nazwa_U.click()
Nazwa_U.clear()
Nazwa_U.send_keys("NNNNĄ")
Email.click()

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Nazwa użytkownika"
try:
    T3_E_NU = driver.find_element(By.ID, "UserName-error")
    if T3_E_NU:
        if T3_E_NU.text != "Nazwa użytkownika powinna zawierać minimum 5 znaków, składać się z liter" \
                           " (bez polskich ogonków), cyfr, myślników lub znaków podkreślenia i nie może " \
                           "zawierać samych cyfr":
            T3_E1 = "Tekst informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Nazwa użytkownika powinna zawierać minimum 5 znaków, składać się z liter ""\n" \
                    "(bez polskich ogonków), cyfr, myślników lub znaków podkreślenia i nie może zawierać samych cyfr'" "\n" \
                     "Wyświetlony tekst - " + T3_E_NU.text
            T3_E.append(T3_E1)
except:
    T3_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Nazwa użytkownika'"
    T3_E.append(T3_E2)

try:
    T3_C_NU = T3_E_NU.value_of_css_property(property_name= "Color")
    if T3_C_NU:
        if T3_C_NU != "rgb(213, 0, 0)":
            T3_E3 = "Kolor informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T3_C_NU
            T3_E.append(T3_E3)
except:
    T3_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Nazwa użytkownika'"
    T3_E.append(T3_E4)


# Raport z Test 3

print(".....................................................................................................")

if T3_E == []:
    print("Test 3 - Zaliczony")
    T += 1
else:
    print("Test 3 - Wykryto błędy / Niezaliczony")
    for e in T3_E:
        print(e)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 4
# Lista błędów testu 4.

T4_E = []

# Wprowadzenie tekstu do okna tekstowego 'Nazwa użytkownika' i przejście do kolejnego okna tekstowego.
Nazwa_U.click()
Nazwa_U.clear()
Nazwa_U.send_keys("NNNN#")
Email.click()

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Nazwa użytkownika"
try:
    T4_E_NU = driver.find_element(By.ID, "UserName-error")
    if T4_E_NU:
        if T4_E_NU.text != "Nazwa użytkownika powinna zawierać minimum 5 znaków, składać się z liter" \
                           " (bez polskich ogonków), cyfr, myślników lub znaków podkreślenia i nie może " \
                           "zawierać samych cyfr":
            T4_E1 = "Tekst informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Nazwa użytkownika powinna zawierać minimum 5 znaków, składać się z liter ""\n" \
                    "(bez polskich ogonków), cyfr, myślników lub znaków podkreślenia i nie może zawierać samych cyfr'" "\n" \
                     "Wyświetlony tekst - " + T4_E_NU.text
            T4_E.append(T4_E1)
except:
    T4_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Nazwa użytkownika'"
    T3_E.append(T4_E2)

try:
    T4_C_NU = T4_E_NU.value_of_css_property(property_name= "Color")
    if T4_C_NU:
        if T4_C_NU != "rgb(213, 0, 0)":
            T4_E3 = "Kolor informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T4_C_NU
            T4_E.append(T4_E3)
except:
    T4_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Nazwa użytkownika'"
    T4_E.append(T4_E4)


# Raport z Test 4

print(".....................................................................................................")

if T4_E == []:
    print("Test 4 - Zaliczony")
    T += 1
else:
    print("Test 4 - Wykryto błędy / Niezaliczony")
    for e in T4_E:
        print(e)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 5
# Lista błędów testu 5.

T5_E = []

# Wprowadzenie tekstu do okna tekstowego 'Nazwa użytkownika' i przejście do kolejnego okna tekstowego.
Nazwa_U.click()
Nazwa_U.clear()
Nazwa_U.send_keys("12345")
Email.click()

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Nazwa użytkownika"
try:
    T5_E_NU = driver.find_element(By.ID, "UserName-error")
    if T5_E_NU:
        if T5_E_NU.text != "Nazwa użytkownika powinna zawierać minimum 5 znaków, składać się z liter" \
                           " (bez polskich ogonków), cyfr, myślników lub znaków podkreślenia i " \
                           "nie może zawierać samych cyfr":
            T5_E1 = "Tekst informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Nazwa użytkownika powinna zawierać minimum 5 znaków, składać się z liter ""\n" \
                    "(bez polskich ogonków), cyfr, myślników lub znaków podkreślenia i nie może zawierać samych cyfr'" "\n" \
                     "Wyświetlony tekst - " + T5_E_NU.text
            T5_E.append(T5_E1)
except:
    T5_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Nazwa użytkownika'"
    T5_E.append(T5_E2)

try:
    T5_C_NU = T5_E_NU.value_of_css_property(property_name= "Color")
    if T5_C_NU:
        if T5_C_NU != "rgb(213, 0, 0)":
            T5_E3 = "Kolor informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T5_C_NU
            T5_E.append(T5_E3)
except:
    T5_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Nazwa użytkownika'"
    T5_E.append(T5_E4)


# Raport z Test 5

print(".....................................................................................................")

if T5_E == []:
    print("Test 5 - Zaliczony")
    T += 1
else:
    print("Test 5 - Wykryto błędy / Niezaliczony")
    for e in T5_E:
        print(e)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 6
# Lista błędów testu 6.

T6_E = []

# Wprowadzenie tekstu do okna tekstowego 'Nazwa użytkownika', usunięcie go i przejście do kolejnego okna tekstowego.
Nazwa_U.click()
Nazwa_U.clear()
Nazwa_U.send_keys("NNNNNN")
Nazwa_U.clear()
Email.click()

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Nazwa użytkownika"
try:
    T6_E_NU = driver.find_element(By.ID, "UserName-error")
    if T6_E_NU:
        if T6_E_NU.text != "Pole wymagane":
            T6_E1 = "Tekst informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Pole wymagane'" "\n" \
                     "Wyświetlony tekst - " + T6_E_NU.text
            T6_E.append(T6_E1)
except:
    T6_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Nazwa użytkownika'"
    T6_E.append(T6_E2)

try:
    T6_C_NU = T6_E_NU.value_of_css_property(property_name= "Color")
    if T6_C_NU:
        if T6_C_NU != "rgb(213, 0, 0)":
            T6_E3 = "Kolor informacji o błędzie pod polem testowym 'Nazwa użytkownika' niezgodny z wytycznymi.""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T6_C_NU
            T6_E.append(T6_E3)
except:
    T6_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Nazwa użytkownika'"
    T6_E.append(T6_E4)


# Raport z Test 6

print(".....................................................................................................")

if T6_E == []:
    print("Test 6 - Zaliczony")
    T += 1
else:
    print("Test 6 - Wykryto błędy / Niezaliczony")
    for e in T6_E:
        print(e)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 7
# Lista błędów testu 7.

T7_E = []

# Wprowadzenie tekstu do okna tekstowego 'Email' i przejście do kolejnego okna tekstowego.
Email.click()
Email.send_keys("adres#gmail.com")
Hasło.click()

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Adres e-mail"
try:
    T7_E_E = driver.find_element(By.ID, "Email-error")
    if T7_E_E:
        if T7_E_E.text != "Nieprawidłowy format adresu e-mail":
            T7_E1 = "Tekst informacji o błędzie pod polem testowym 'E-mail' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Nieprawidłowy format adresu e-mail'" "\n" \
                     "Wyświetlony tekst - " + T7_E_E.text
            T7_E.append(T7_E1)
except:
    T7_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'E-mail'"
    T7_E.append(T7_E2)

try:
    T7_C_E = T7_E_E.value_of_css_property(property_name= "Color")
    if T7_C_E:
        if T7_C_E != "rgb(213, 0, 0)":
            T7_E3 = "Kolor informacji o błędzie pod polem testowym 'E-mail' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T7_C_E
            T7_E.append(T7_E3)
except:
    T7_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'E-mail'"
    T7_E.append(T7_E4)

# Raport z Test 7

print(".....................................................................................................")

if T7_E == []:
    print("Test 7 - Zaliczony")
    T += 1
else:
    print("Test 7 - Wykryto błędy / Niezaliczony")
    for e in T7_E:
        print(e)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 8
# Lista błędów testu 8.

T8_E = []

# Wprowadzenie tekstu do okna tekstowego 'Email', usunięcie go i przejście do kolejnego okna tekstowego.
Email.click()
Email.clear()
Email.send_keys("adres@gmail.com")
Email.clear()
Hasło.click()

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Adres e-mail"
try:
    T8_E_E = driver.find_element(By.ID, "Email-error")
    if T8_E_E:
        if T8_E_E.text != "Pole wymagane":
            T8_E1 = "Tekst informacji o błędzie pod polem testowym 'E-mail' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Pole wymagane'" "\n" \
                     "Wyświetlony tekst - " + T8_E_E.text
            T8_E.append(T8_E1)
except:
    T8_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'E-mail'"
    T8_E.append(T8_E2)

try:
    T8_C_E = T8_E_E.value_of_css_property(property_name= "Color")
    if T8_C_E:
        if T8_C_E != "rgb(213, 0, 0)":
            T8_E3 = "Kolor informacji o błędzie pod polem testowym 'E-mail' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T8_C_E
            T8_E.append(T8_E3)
except:
    T8_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'E-mail'"
    T8_E.append(T8_E4)

# Raport z Test 8

print(".....................................................................................................")

if T8_E == []:
    print("Test 8 - Zaliczony")
    T += 1
else:
    print("Test 8 - Wykryto błędy / Niezaliczony")
    for e in T8_E:
        print(e)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 9
# Lista błędów testu 9.

T9_E = []

# Wprowadzenie zbyt krótkiego tekstu do okna tekstowego 'Hasło' i przejście do kolejnego okna tekstowego.
Hasło.click()
Hasło.send_keys("HHHHH")
P_Hasło.click()

# Pobranie informacji o błędzie pod polem tekstowym "Hasło"
try:
    T9_E_H = driver.find_element(By.ID, "Password-error")
    if T9_E_H:
        if T9_E_H.text != "Hasło powinno zawierać minimum 6 znaków":
            T9_E1 = "Tekst informacji o błędzie pod polem testowym 'Hasło' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Hasło powinno zawierać minimum 6 znaków'" "\n" \
                     "Wyświetlony tekst - " + T9_E_H.text
            T9_E.append(T9_E1)
except:
    T9_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Hasło'"
    T9_E.append(T9_E2)

try:
    T9_C_H = T9_E_H.value_of_css_property(property_name= "Color")
    if T9_C_H:
        if T9_C_H != "rgb(213, 0, 0)":
            T9_E3 = "Kolor informacji o błędzie pod polem testowym 'Hasło' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T9_C_H
            T9_E.append(T9_E3)
except:
    T9_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Hasło'"
    T9_E.append(T9_E4)

# Raport z Test 9

print(".....................................................................................................")

if T9_E == []:
    print("Test 9 - Zaliczony")
    T += 1
else:
    print("Test 9 - Wykryto błędy / Niezaliczony")
    for e in T9_E:
        print(e)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 10
# Lista błędów testu 10.

T10_E = []

# Wprowadzenie do pola tekstowego „Hasło” tekstu spełniającego wymagania i następnie jego usunięcie.
Hasło.click()
Hasło.clear()
Hasło.send_keys("HHHHHH")
Hasło.clear()
P_Hasło.click()

# Pobranie informacji o błędzie pod polem tekstowym "Hasło"
try:
    T10_E_H = driver.find_element(By.ID, "Password-error")
    if T10_E_H:
        if T10_E_H.text != "Pole wymagane":
            T10_E1 = "Tekst informacji o błędzie pod polem testowym 'Hasło' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Pole wymagane'" "\n" \
                     "Wyświetlony tekst - " + T10_E_H.text
            T10_E.append(T10_E1)
except:
    T10_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Hasło'"
    T10_E.append(T10_E2)

try:
    T10_C_H = T10_E_H.value_of_css_property(property_name="Color")
    if T10_C_H:
        if T10_C_H != "rgb(213, 0, 0)":
            T10_E3 = "Kolor informacji o błędzie pod polem testowym 'Hasło' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T10_C_H
            T10_E.append(T9_E3)
except:
    T10_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Hasło'"
    T10_E.append(T10_E4)

# Raport z Test 10

print(".....................................................................................................")

if T10_E == []:
    print("Test 10 - Zaliczony")
    T += 1
else:
    print("Test 10 - Wykryto błędy / Niezaliczony")
    for e in T10_E:
        print(e)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 11
# Lista błędów testu 11.

T11_E = []

# Wprowadzenie do pól tekstowych „Hasło” i „Powtórz hasło” różnych tekstów i przejście do innego okna testowego.
Hasło.click()
Hasło.clear()
Hasło.send_keys("HHHHHH")
P_Hasło.click()
P_Hasło.send_keys("PPPPPP")
Email.click()

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Powtórz hasło"
try:
    T11_E_PH = driver.find_element(By.ID, "ConfirmPassword-error")
    if T11_E_PH:
        if T11_E_PH.text != "Podane hasła nie sa identyczne":
            T11_E1 = "Tekst informacji o błędzie pod polem testowym 'Powtórz hasło' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Podane hasła nie sa identyczne'" "\n" \
                     "Wyświetlony tekst - " + T11_E_PH.text
            T11_E.append(T11_E1)
except:
    T11_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Powtórz hasło'"
    T11_E.append(T11_E2)

try:
    T11_C_PH = T11_E_PH.value_of_css_property(property_name= "Color")
    if T11_C_PH:
        if T11_C_PH != "rgb(213, 0, 0)":
            T11_E3 = "Kolor informacji o błędzie pod polem testowym 'Powtórz hasło' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T11_C_PH
            T11_E.append(T11_E3)
except:
    T11_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Powtórz hasło'"
    T11_E.append(T11_E4)

# Raport z Test 11

print(".....................................................................................................")

if T11_E == []:
    print("Test 11 - Zaliczony")
    T += 1
else:
    print("Test 11 - Wykryto błędy / Niezaliczony")
    for e in T11_E:
        print(e)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 12
# Lista błędów testu 12.

T12_E = []

# Wprowadzenie do pól tekstowych „Hasło” i „Powtórz hasło” takich samych tekstów, usunięcie tekstu z pola
# „Powtórz hasło” i następnie przejście do innego okna.
Hasło.click()
Hasło.clear()
Hasło.send_keys("HHHHHH")
P_Hasło.click()
P_Hasło.clear()
P_Hasło.send_keys("HHHHHH")
P_Hasło.clear()
Email.click()

# Pobranie i sprawdzenie poprawności informacji o błędzie pod polem tekstowym "Powtórz hasło"
try:
    T12_E_PH = driver.find_element(By.ID, "ConfirmPassword-error")
    if T12_E_PH:
        if T12_E_PH.text != "Pole wymagane":
            T12_E1 = "Tekst informacji o błędzie pod polem testowym 'Powtórz hasło' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Pole wymagane'" "\n" \
                     "Wyświetlony tekst - " + T12_E_PH.text
            T12_E.append(T12_E1)
except:
    T12_E2 = "Nie znaleziono informacji o błędzie pod polem tekstowym 'Powtórz hasło'"
    T12_E.append(T12_E2)

try:
    T12_C_PH = T12_E_PH.value_of_css_property(property_name= "Color")
    if T12_C_PH:
        if T12_C_PH != "rgb(213, 0, 0)":
            T12_E3 = "Kolor informacji o błędzie pod polem testowym 'Powtórz hasło' niezgodny z wytycznymi""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T12_C_PH
            T12_E.append(T12_E3)
except:
    T12_E4 = "Nie znaleziono informacji o kolorze tekstu pod polem tekstowym 'Powtórz hasło'"
    T12_E.append(T12_E4)

# Raport z Test 12

print(".....................................................................................................")

if T12_E == []:
    print("Test 12 - Zaliczony")
    T += 1
else:
    print("Test 12 - Wykryto błędy / Niezaliczony")
    for e in T12_E:
        print(e)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Test 13
# Lista błędów testu 13.

T13_E = []

#Zaznaczenie i następnie odznaczenie checkboxa „Akceptacja regulaminu”

Akceptacja.click()
Akceptacja.click()

# Pobranie informacji o błędzie pod checkboxem  "Akceptacja regulaminu"

try:
    T13_E_AR = driver.find_element(By.ID, "AcceptDiscipline-error")
    if T13_E_AR:
        if T13_E_AR.text != "Zgoda obowiązkowa. Zaznacz to pole, jeśli chcesz kontynuować":
            T13_E1 = "Tekst informacji o błędzie pod checkboxem 'Akceptacja regulaminu' niezgodny z wytycznymi""\n" \
                     "Oczekiwany tekst - 'Zgoda obowiązkowa. Zaznacz to pole, jeśli chcesz kontynuować'" "\n" \
                     "Wyświetlony tekst - " + T13_E_AR.text
            T13_E.append(T13_E1)
except:
    T13_E2 = "Nie znaleziono informacji o błędzie pod checkboxem 'Akceptacja regulaminu'"
    T13_E.append(T13_E2)

try:
    T13_C_AR = T13_E_AR.value_of_css_property(property_name= "Color")
    if T13_C_AR:
        if T13_C_AR != "rgb(213, 0, 0)":
            T13_E3 = "Kolor informacji o błędzie pod checkboxem 'Akceptacja regulaminu' niezgodny z wytycznymi.""\n" \
                     "Kolor oczekiwany - rgb(213,0,0)""\n" \
                     "Kolor tekstu - " + T13_C_AR
            T13_E.append(T13_E3)

except:
    T13_E4 = "Nie znaleziono informacji o kolorze tekstu pod checkboxem 'Akceptacja regulaminu'"
    T13_E.append(T13_E4)


# Raport z Test 13

print(".....................................................................................................")

if T13_E == []:
    print("Test 13 - Zaliczony")
    T += 1
else:
    print("Test 13 - Wykryto błędy / Niezaliczony")
    for e in T13_E:
        print(e)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Podsumowanie

if T == 13:
    print("....................................................................................""\n"
          "PODSUMOWANIE""\n"
          "Wszystkie testy zostały przeprowadzone pomyślnie""\n"
          "Nie wykryto błędów")
else:
    print("....................................................................................""\n"
          "PODSUMOWANIE""\n"
          "Podczas przeprowadzania testów wykryto błędy.""\n"
          "Należy przeprowadzić ich analizę.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Zamykanie strony Legimi

driver.close()


input("Naciśnij ENTER, żeby zakończyć test")
exit()