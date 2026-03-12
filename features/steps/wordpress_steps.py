from behave import given, when, then
from pages.wordpress_page import WordPressPage
from pages.themes_page import ThemesPage


import time

@given("Launch the WordPress website")
def step_launch(context):
    context.page = WordPressPage(context.driver)
    context.page.open_site()

@then("Verify the page title")
def step_verify_title(context):

    expected = "WordPress.org"
    actual = context.page.get_title()

    assert expected in actual

@when("Mouse hover on Extend")
def step_hover(context):

    context.page.hover_download_extend()
    time.sleep(2)

@when("Click on Themes")
def step_click_theme(context):

    context.page.click_themes()
    time.sleep(2)

    # initialize ThemesPage
    context.themes_page = ThemesPage(context.driver)


@then("Verify themes page is displayed")
def step_verify_theme(context):

    assert "Theme" in context.driver.title

@when('Search for theme "{theme}"')
def step_search(context, theme):
    context.themes_page.search_theme(theme)
    time.sleep(3)


@then("Verify themes are displayed")
def step_verify_themes(context):

    result = context.themes_page.get_theme_title()

    assert result