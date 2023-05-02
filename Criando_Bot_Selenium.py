# chrome -> chomedriver - ou -
# firefox -> geckodriver

from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get("https://login.live.com/")

time.sleep(1.5)

navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys("exemplo@outlook.com")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()

time.sleep(1.5)

navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys("exemplo123123")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()