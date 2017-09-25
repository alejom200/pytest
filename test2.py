
import splinter
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#selenium = webselenium.Firefox()
#@pytest.fixture

def test_load_webpage(session_browser):
    session_browser.visit("http://www.google.com")
    assert "Google" in session_browser.title
    elem = session_browser.find_by_name("q")
    elem.clear()
    elem.type("Hurricane News")
    elem.type(Keys.RETURN)
    assert session_browser.is_text_not_present("No results found.")
    time.sleep(3)


def test_load_webpage2(session_browser):
    session_browser.visit("http://www.python.org")
    assert "Python" in session_browser.title
    elem = session_browser.find_by_name("q")
    elem.clear()
    elem.type("pycon")
    elem.type(Keys.RETURN)
    assert session_browser.is_text_not_present("No results found.")
    time.sleep(3)

