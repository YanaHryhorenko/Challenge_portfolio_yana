from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button/span[1]"
    select_language_button_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
