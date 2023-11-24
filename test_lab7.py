import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from psutil import process_iter

class PikabuTesting(unittest.TestCase):

    def setUp(self):
        opt = webdriver.FirefoxOptions()
        opt.set_preference("browser.link.open_newwindow", 1)
        self.driver = webdriver.Firefox(opt)
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
    
    def IsGoogleAdAppearsInThisBrowser(self):
        for proc in process_iter():
            if "geckodriver" in proc.name():
                return True
        return False

    def IsElementExistOnPage(self, by, value):
        return len(self.driver.find_elements(by, value)) > 0

    def RemoveGoogleAd(self):
        driver = self.driver
        if not self.IsGoogleAdAppearsInThisBrowser():
            return
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#google-one-tap-container'))
        )
        while self.IsElementExistOnPage(By.CSS_SELECTOR, '#google-one-tap-container iframe'):
            driver.find_element(By.CSS_SELECTOR, 'header').click()

    def Autorize(self):
        driver = self.driver
        driver.find_element(
            By.CSS_SELECTOR, 
            '#signin-form input[name="username"]'
        ).send_keys("FancyHamster")
        driver.find_element(
            By.CSS_SELECTOR, 
            '#signin-form input[name="password"]'
        ).send_keys("),mGVht8Pm7^diB")
        driver.find_element(
            By.CSS_SELECTOR, 
            '#signin-form button[type="submit"]'
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.user_right-sidebar .user__nick'))
        )


    # def test_auth_with_wrong_credentials(self):
    #     driver = self.driver
    #     driver.get("https://pikabu.ru/")
    #     self.RemoveGoogleAd()
    #     driver.find_element(
    #         By.CSS_SELECTOR, 
    #         '#signin-form input[name="username"]'
    #     ).send_keys("yoasdf")
    #     driver.find_element(
    #         By.CSS_SELECTOR, 
    #         '#signin-form input[name="password"]'
    #     ).send_keys("youu")
    #     driver.find_element(
    #         By.CSS_SELECTOR,
    #         '#signin-form button[type="submit"]'
    #     ).click()
    #     WebDriverWait(driver, 10).until( 
    #         EC.visibility_of_element_located((By.CSS_SELECTOR,'#signin-form .auth__error'))
    #     )
    #     elem = driver.find_element(By.CSS_SELECTOR, '#signin-form .auth__error')
    #     self.assertEqual('Ошибка. Вы ввели неверные данные авторизации', elem.text)
    #     sleep(10)

    # def test_auth_with_right_credentials(self):
    #     driver = self.driver
    #     driver.get("https://pikabu.ru/")
    #     self.RemoveGoogleAd()
    #     self.Autorize()
    #     elem = driver.find_element(By.CSS_SELECTOR, '.user_right-sidebar .user__nick')
    #     self.assertEqual('FancyHamster', elem.text)
    #     sleep(10)

    def SearchContentInSite(self, searchQuery):
        driver = self.driver
        while not self.IsElementExistOnPage(By.CSS_SELECTOR, '.header-right-menu__search_focus'):
            driver.find_element(By.CSS_SELECTOR, '.header-right-menu__search button[type=submit]').click()
        WebDriverWait(driver, 5).until( 
            EC.visibility_of_element_located((By.NAME,'q'))
        )
        driver.find_element(By.NAME, 'q').send_keys(searchQuery)
        while self.IsElementExistOnPage(By.CSS_SELECTOR, '.header-right-menu__search_focus'):
            driver.find_element(By.CSS_SELECTOR, '.header-right-menu__search button[type=submit]').click()
            sleep(1)

    # def test_search_for_not_existing_content(self):
    #     driver = self.driver
    #     driver.get("https://pikabu.ru/")
    #     self.RemoveGoogleAd()
    #     self.SearchContentInSite('adlskfjdsalfjadslkf')
    #     self.RemoveGoogleAd()
    #     elem = driver.find_element(By.CSS_SELECTOR, '.stories-feed__message')
    #     self.assertEqual('Посты не найдены', elem.text)
    #     sleep(10)

    # def test_search_for_existing_content(self):
    #     driver = self.driver
    #     driver.get("https://pikabu.ru/")
    #     self.RemoveGoogleAd()
    #     self.SearchContentInSite('hamster')
    #     self.RemoveGoogleAd()
    #     driver.find_element(By.CSS_SELECTOR, '.story:first-of-type')
    #     sleep(10)

    # def test_give_upvote_to_article(self):
    #     driver = self.driver
    #     driver.get("https://pikabu.ru/")
    #     self.RemoveGoogleAd()
    #     self.Autorize()
    #     self.SearchContentInSite('hamster')
    #     amountOfLikesBefore = driver.find_element(
    #         By.CSS_SELECTOR, 
    #         '.story__rating-count'
    #     ).text
    #     elem = driver.find_element(
    #         By.CSS_SELECTOR,
    #         '.story__rating-up'
    #     )
    #     elem.click()
    #     amountOfLikesAfter = elem.text
    #     self.assertNotEqual(amountOfLikesBefore, amountOfLikesAfter)
    #     driver.find_element(
    #         By.CSS_SELECTOR,
    #         '.story__rating-up'
    #     ).click()
    #     sleep(10)

    def SearchFirstArticleWithTitle(self, title):
        driver = self.driver
        self.SearchContentInSite(title)
        driver.find_element(By.CSS_SELECTOR, 'article.story:first-of-type .story__title a').click()
        while len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    def NavigateToCommentsSectionOfArticle(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '.story__tools .story__comments-link').click()
        while len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    
    # def test_leave_comment_to_article(self):
    #     driver = self.driver
    #     driver.get("https://pikabu.ru/")
    #     self.RemoveGoogleAd()
    #     self.Autorize()
    #     self.SearchFirstArticleWithTitle('hamster')
    #     self.NavigateToCommentsSectionOfArticle()
    #     WebDriverWait(driver, 50).until( 
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, '.input__input p'))
    #     )
    #     elem = driver.find_element(By.CSS_SELECTOR, '.input__input p')
    #     elem.click()
    #     actions = ActionChains(driver)
    #     actions.send_keys('adsf')
    #     actions.perform()
    #     driver.find_element(
    #         By.CSS_SELECTOR, 
    #         '.comment-reply__controls .button_success'
    #     ).click()
    #     WebDriverWait(driver, 50).until( 
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, '.comment__controls .button_link[data-type="remove"]'))
    #     )
    #     driver.find_element(
    #         By.CSS_SELECTOR, 
    #         '.comment__controls .button_link[data-type="remove"]'
    #     ).click()
    #     sleep(10)

    # def test_give_upvote_to_comment(self):
    #     driver = self.driver
    #     driver.get("https://pikabu.ru/")
    #     self.RemoveGoogleAd()
    #     self.Autorize()
    #     self.SearchFirstArticleWithTitle('hamster')
    #     self.NavigateToCommentsSectionOfArticle()
    #     WebDriverWait(driver, 50).until( 
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, '.comment__rating-up'))
    #     )
    #     #"unliking" all comments 
    #     while self.IsElementExistOnPage(By.CSS_SELECTOR, '.comment__rating-up_active'):
    #         driver.find_element(By.CSS_SELECTOR, '.comment__rating-up_active').click()
    #     elem = driver.find_element(By.CSS_SELECTOR, '.comment__rating-up')
    #     elem.click()
    #     WebDriverWait(driver, 10).until( 
    #         EC.element_to_be_clickable((
    #             By.CSS_SELECTOR, 
    #             '.comment__rating-up_active'
    #         ))
    #     )
    #     sleep(10)
    #     elem.click()

if __name__ == "__main__":
    unittest.main()