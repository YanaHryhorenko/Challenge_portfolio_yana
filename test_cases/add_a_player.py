import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.add_a_player import AddPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        add_player_page = AddPlayer(self.driver)
        add_player_page.click_on_the_add_player_button()




    @classmethod
    def tearDown(self):
        self.driver.quit()