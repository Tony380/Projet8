from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys


class TestApp(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_index_page(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element_by_class_name('text-center')
        self.assertEquals(
            alert.find_element_by_tag_name('h2').text,
            'Trouvez un produit de substitution '
            'pour ceux que vous consommez tous les jours'
        )

    def test_register_form_submission_with_button(self):

        self.browser.get(str(self.live_server_url) + '/user/register')
        username_input = self.browser.find_element_by_id('id_username')
        email_input = self.browser.find_element_by_id('id_email')
        password1_input = self.browser.find_element_by_id('id_password1')
        password2_input = self.browser.find_element_by_id('id_password2')
        submission_button = self.browser.find_element_by_class_name(
            'btn-primary')

        username_input.send_keys('username')
        email_input.send_keys('email@gmail.com')
        password1_input.send_keys('abcdef123')
        password2_input.send_keys('abcdef123')
        submission_button.click()
        redirection_url = self.browser.current_url

        self.assertEqual(self.live_server_url + '/user/register',
                         redirection_url)

    def test_login_form_submission_with_enter_key(self):
        self.browser.get(str(self.live_server_url) + '/user/login')
        username_input = self.browser.find_element_by_id('id_username')
        password_input = self.browser.find_element_by_id('id_password')
        submission_button = self.browser.find_element_by_class_name(
            'btn-primary')

        username_input.send_keys('username')
        password_input.send_keys('abcdef123')
        submission_button.send_keys(Keys.ENTER)
        redirection_url = self.browser.current_url

        self.assertEqual(self.live_server_url + '/user/login', redirection_url)
