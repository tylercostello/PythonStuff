from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://www10.goiania.go.gov.br/TransWeb/FuncionariosExportarPopUp.aspx?_=1590514086637')
element = driver.find_element_by_id('WebPatterns_wt12_block_wtMainContent_wtcboReferencia')
all_options = element.find_elements_by_tag_name("option")
selectYear = Select(driver.find_element_by_id("WebPatterns_wt12_block_wtMainContent_wtcboReferencia"))
link = driver.find_element_by_id('WebPatterns_wt12_block_wtMainContent_wtbtnGerar')
for option in all_options[:267]:
    print("Value is: %s" % option.get_attribute("value"))
    selectYear.select_by_value(option)
    link.click()
    time.sleep(5000)
