import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

message = 'Congratulations! You have successfully registered!'
first_name = 'Roman'
last_name = 'Smirnov'
email = 'roman_smirnov@yandex.ru'


class TestRegistrationForm(unittest.TestCase):

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.binary_location = brave_path
        self.driver = webdriver.Chrome(options=option)

    def tearDown(self):
        self.driver.quit()

    def fill_form(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CLASS_NAME, "first[required]").send_keys(first_name)
        self.driver.find_element(By.CLASS_NAME, "second[required]").send_keys(last_name)
        self.driver.find_element(By.CLASS_NAME, "third[required]").send_keys(email)

        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        return self.driver.find_element(By.TAG_NAME, 'h1').text

    def test_form(self):
        # Arrange
        urls = [
            "https://suninjuly.github.io/registration1.html",
            "https://suninjuly.github.io/registration2.html"
        ]

        for url in urls:
            with self.subTest(url=url):
                # Act
                registration_result = self.fill_form(url)

                # Assert
                self.assertEqual(message, registration_result, f"expected {message}, got {registration_result}")


    def test_form2(self):
        # Arrange
        link = "https://suninjuly.github.io/registration2.html"

        # Act
        registration_result = self.fill_form(link)

        # Assert
        self.assertEqual(message, registration_result, f"expected {message}, got {registration_result}")


if __name__ == "__main__":
    unittest.main()
