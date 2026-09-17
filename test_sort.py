from playwright.sync_api import Page, expect

def test_price_sorting(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator(".inventory_list")).to_be_visible()
    # сортировка товаров
    page.locator(".product_sort_container").select_option("lohi")
    #собираем все цены товаров со страницы в виде списка строк
    price_elements = page.locator(".inventory_item_price").all_text_contents()
    prices = [float(price[1:]) for price in price_elements]
    print(f"\nЦены после сортировки: {prices}")

    # проверяем что список отсортирован
    assert prices == sorted(prices)