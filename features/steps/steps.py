from behave import *
from selenium.webdriver import Keys

from features.utils import *


@step('открываем сайт "{site}"')
def open_site(context, site):
    context.drv.get(site)
    context.drv.maximize_window()
    time.sleep(2)
    title_site = context.drv.title[0:25]
    title = 'Регард - интернет магазин'
    assert title_site == title, f'Заглавие сайта не совпадает: *{title_site}*!'


@step('открываем каталог {section} и {sub_section}')
def submenu(context, section, sub_section):
    find_element(context, regard_locators.get("button_catalog")).click()
    catalog_name = regard_locators.get("catalog_name").replace('section_old', section)
    find_element(context, catalog_name).click()
    sub_catalog_name = regard_locators.get("sub_catalog_name").replace('sub_section_old', sub_section)
    find_element(context, sub_catalog_name).click()


@step('устанавливаем фильтр цена: {min_max_price} значение цены: {price} и производитель: {company}')
def input_filter(context, min_max_price, price, company):
    min_or_max = regard_locators.get("min_or_max_price").replace('min_max', min_max_price)
    find_element(context, min_or_max).send_keys(price)
    find_element(context, regard_locators.get("all_company")).click()
    company_name = regard_locators.get("company_name").replace('company_old', company)
    find_element(context, company_name).click()
    loading(context)


@step('проверяем кол.во найденных товаров на странице')
def prod_on_page(context):
    products_on_page = find_element(context, regard_locators.get("prod_on_page")).text
    products_of_page = "по 24"
    assert products_on_page == products_of_page, \
        f'На странице отображается: *{products_on_page}*, а должно: *{products_of_page}*!'


@step('копируем название первого товара и вставляем его в строку поиска')
def search_first_product(context):
    first_product = context.drv.find_element(By.XPATH, regard_locators.get("first_product_name")).text
    find_element(context, regard_locators.get("search_input")).send_keys(first_product)
    find_element(context, regard_locators.get("search_input")).send_keys(Keys.ENTER)
    loading(context)


@step('снова проверяем кол.во найденных товаров на странице')
def accert_amount_product(context):
    amount_product_search = find_element(context, regard_locators.get("amount_prod_search")).text
    products_of_page = "1 товар"
    assert amount_product_search == products_of_page, \
        f'На странице отображается: *{amount_product_search}*, а должен: *{products_of_page}*!'


@step('проверяем, что найденный товар соответствует товару, вставленному в строку поиска')
def accert_seach_product(context):
    name_first_value = find_element(context, regard_locators.get("first_product_name")).text
    search_product = find_element(context, regard_locators.get("search_input")).get_attribute('value')
    assert search_product == name_first_value, \
        f'Найденный товар *{name_first_value}* не соответствует товару, вставленному в поиск *{search_product}*!'
