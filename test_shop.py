import pytest
from playwright.sync_api import Page, expect

login_test_date = [
    ("standard_user", "secret_sauce", "success"),
    ("locked_out_user", "secret_sauce", "error"),
    ("problem_user","secret_sauce", "success"),
    ("Oleg", "dff", "error"),
]

@pytest.mark.parametrize("username, password, expected_result", login_test_date)
def test_saucedemo_login_parametrized(page: Page, username: str, password: str, expected_result: str):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    if expected_result == "success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.locator(".inventory_list")).to_be_visible()
        page.locator("#add-to-cart-sauce-labs-backpack").click()
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")

        page.locator(".shopping_cart_link").click()
        expect(page.locator(".title")).to_have_text("Your Cart")

        page.locator("#checkout").click()

        page.locator("#first-name").fill("Alex")
        page.locator("#last-name").fill("Cooper")
        page.locator("#postal-code").fill("2345")
        page.locator("#continue").click()
        page.locator("#finish").click()
        expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
    elif expected_result == "error":
        expect(page.locator("[data-test='error']")).to_be_visible()
        expect(page).to_have_url("https://www.saucedemo.com/")


