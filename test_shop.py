from playwright.sync_api import Page, expect

def test_complete_purchase_flow(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

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
