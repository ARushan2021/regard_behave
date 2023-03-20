import time

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# behave -i test_regard.feature
@step('open website {website}')
def step_one(self, website):
    self.drv = webdriver.Chrome('chromedriver.exe')
    self.drv.get(website)
    self.drv.maximize_window()
    time.sleep(2)
    titlesite = self.drv.title
    title = 'Регард - интернет магазин компьютеров и комплектующих, техники для офиса и электроники. Сборка ПК. Доставка по России'
    assert titlesite == title
    time.sleep(2)

@step('open subsection {section} and subsection {sub_section}')
def submenu(self, section, sub_section):
    # Нажимаем кнопку каталог
    self.drv.find_element(By.XPATH, "//button[contains(@class, 'NavigationBar_burgerButton')]").click()
    time.sleep(2)
    # Нажимаем на раздел в каталоге
    self.drv.find_element(By.XPATH, "//div[text()='" + section + "']/ancestor::a").click()
    time.sleep(2)
    # Нажимем на нужный раздел
    self.drv.find_element(By.XPATH, "//div/p[contains(text(),'" + sub_section + "')]").click()
    time.sleep(2)

@step('put the filter on min price: {min_price} and company: {company}')
def input_filter(self, min_price, company):
    # Ставим фильтр по минимальной цене
    self.drv.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div/div[1]/section/div[2]/div/div/div/div/input[@name='min']").send_keys(min_price)
    time.sleep(2)
    # Разворачиваем список всех производителей
    self.drv.find_element(By.XPATH, "//li/span[@class='ListingFilters_showMore__btn__dw-Xb']").click()
    # Выбираем нужного производителя
    self.drv.find_element(By.XPATH, "//label[text()='" + company + "']").click()
    time.sleep(2)

@step('assert count products on the page')
def prod_on_page(self):
    products_on_page = self.drv.find_element(By.XPATH, "//span[@class='Pagination_countSetter__count__3f3n_']").text
    assert products_on_page == "по 24"
    time.sleep(2)

@step('the first product found in the search')
def seach_first_priduct(self):
    self.first_priduct = self.drv.find_element(By.XPATH, "//div[contains(@class,'CardText_wrap__1wwDN')]/a/h6").text
    self.drv.find_element(By.XPATH, "//*[@id='searchInput']").send_keys(self.first_priduct)
    self.drv.find_element(By.XPATH, "//*[@id='searchInput']").send_keys(Keys.ENTER)
    time.sleep(2)

@step('assert count products on the page 2')
def accert_amount_priduct(self):
    amount_priduct_seach = self.drv.find_element(By.XPATH, "//span[contains(@class, 'ListingLayout_count')]").text
    assert amount_priduct_seach == "1 товар"
    time.sleep(2)
@step('assert first seach product')
def accert_seach_priduct(self):
    name_first_value = self.drv.find_element(By.XPATH, "//div[contains(@class,'CardText_wrap__1wwDN')]/a/h6").text
    assert self.first_priduct == name_first_value
    time.sleep(2)











