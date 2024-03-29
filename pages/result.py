"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
  
  RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
  SEARCH_INPUT = (By.ID, 'search_form_input')
  
  def __init__(self, browser):
    self.browser = browser

  def result_link_titles(self):
    # TODO
    return []
  
  def search_input_value(self):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    value = search_input.get_attribute('value')
    return value

  def title(self):
    return self.browser.title