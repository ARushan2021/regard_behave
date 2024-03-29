Feature: Тестирование regard.ru

  @ProductSearch
  Scenario Outline: Поиск товаров на сайте

    Given открываем сайт "http://regard.ru"
    When открываем каталог <section> и <sub_section>
    When устанавливаем фильтр цена: <min_max_price> значение цены: <price> и производитель: <company>
    When проверяем кол.во найденных товаров на странице
    When копируем название первого товара и вставляем его в строку поиска
    When снова проверяем кол.во найденных товаров на странице
    #When проверяем, что найденный товар соответствует товару, вставленному в строку поиска

    Examples: Поиск товара на regard.ru
      | section              | sub_section | min_max_price | price | company |
      | Периферия            | Мониторы    | max           | 50000 | Samsung |
      | Периферия            | Мыши        | min           | 2000   | A4Tech  |
      | Комплектующие для ПК | Видеокарты  | min           | 500000 | ASUS    |


  # behave --no-capture -запуск теста behave с print() в terminal
  # behave -f allure_behave.formatter:AllureFormatter -o reports/ features  - запуск теста и формирование reports в json
  # allure serve reports/  -формирование reports в html
