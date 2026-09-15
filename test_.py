from playwright.sync_api import Page, expect


def test_saucedemo_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator(".inventory_list")).to_be_visible()
