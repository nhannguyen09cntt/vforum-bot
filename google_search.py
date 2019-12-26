from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time


class GoogleSeach:
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        # self.driver = webdriver.Chrome('./chromedriver')

    def chatbot_query(self, topic, index=0):
        result = ''
        title = topic["title"]
        result = self.find_answer(title)
        self.reply_question(topic["url"], result)
        time.sleep(5)
        return result

    def find_answer(self, query, index=0):
        self.driver.get("https://google.com.vn")
        try:
            elem = self.driver.find_element_by_name("q")
            elem.send_keys(query)
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            search_result = self.driver.find_element_by_id("search")
            answer_link = search_result.find_elements_by_xpath(
                "//*[contains(text(), 'stackoverflow')]")[0]
            answer_link.click()
            time.sleep(2.4)
            introduction = self.driver.find_element_by_id("answers")
            answer = introduction.find_elements(By.CLASS_NAME, "post-text")[0]
            result = answer.get_attribute('innerHTML')
            return result
        except:
            return ''

    def reply_question(self, url, reply_text):
        try:
            # Step 2) go to 4rum.vn
            self.driver.get(url)
            btn_login = self.driver.find_elements_by_xpath(
                "//*[contains(text(), 'Log In')]")[0]
            btn_login.click()

            # Step 3) Search & Enter the Email or Phone field & Enter Password
            username = self.driver.find_element_by_id("login-account-name")
            password = self.driver.find_element_by_id("login-account-password")
            submit = self.driver.find_element_by_id("login-button")
            username.send_keys("")
            password.send_keys("")

            # Step 4) Click Login
            submit.send_keys(Keys.RETURN)

            # Step 5) Enter the answer
            time.sleep(1)
            create_topic = self.driver.find_elements(
                By.CLASS_NAME, "btn-primary.create")[0]
            create_topic.click()
            text_area = self.driver.find_element_by_class_name(
                'ember-text-area')
            text_area.clear()
            text_area.send_keys(reply_text)
            time.sleep(5)
            reply_control = self.driver.find_element_by_id("reply-control")
            save_or_cancle = reply_control.find_elements(
                By.CLASS_NAME, "create")[0]
            save_or_cancle.click()
            return True
        except:
            return False

    def __del__(self):
        self.driver.close()
